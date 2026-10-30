"""Training and perplexity evaluation, identical for both models."""
import contextlib
import math
import time

import numpy as np
import torch
import torch.nn.functional as F

from .models import build_model, count_parameters
from .utils import hardware_info, save_json, set_seed, timestamp


def amp_context(device, cfg):
    if device.type != "cuda" or not cfg["train"]["amp"]:
        return contextlib.nullcontext(), None
    dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
    return torch.autocast("cuda", dtype=dtype), dtype


def lm_loss(logits, targets, pad_id, reduction="mean"):
    return F.cross_entropy(logits.float().reshape(-1, logits.size(-1)), targets.reshape(-1),
                           ignore_index=pad_id, reduction=reduction)


@torch.no_grad()
def evaluate(model, loader, pad_id, device, cfg, max_len=None):
    """Perplexity = exp(total NLL / number of non-pad target tokens, <eos> included).

    If max_len is given, also returns the mean loss at every absolute position in the story
    (offset of the window + index inside it), used for the loss-vs-position analysis.
    """
    model.eval()
    ctx, _ = amp_context(device, cfg)
    total_nll, total_tokens = 0.0, 0
    pos_sum = np.zeros(max_len or 1)
    pos_cnt = np.zeros(max_len or 1)
    for inputs, targets, offsets in loader:
        inputs, targets = inputs.to(device), targets.to(device)
        with ctx:
            logits, _ = model(inputs)
        nll = lm_loss(logits, targets, pad_id, reduction="none").view(targets.shape)
        mask = targets.ne(pad_id)
        total_nll += nll[mask].sum().item()
        total_tokens += mask.sum().item()
        if max_len:
            positions = offsets.to(device)[:, None] + torch.arange(targets.size(1), device=device)[None]
            keep = mask & positions.lt(max_len)
            np.add.at(pos_sum, positions[keep].cpu().numpy(), nll[keep].cpu().numpy())
            np.add.at(pos_cnt, positions[keep].cpu().numpy(), 1)
    mean_nll = total_nll / total_tokens
    result = {"loss": mean_nll, "ppl": math.exp(mean_nll), "tokens": total_tokens}
    if max_len:
        with np.errstate(invalid="ignore"):
            result["per_position_loss"] = (pos_sum / pos_cnt).tolist()
        result["per_position_count"] = pos_cnt.astype(int).tolist()
    return result


def train_model(cell, cfg, tokenizer, train_loader, val_loader, device, ckpt_path, log=print):
    set_seed(cfg["seed"])
    tcfg = cfg["train"]
    model = build_model(cell, cfg, len(tokenizer), tokenizer.pad_id).to(device)
    params = count_parameters(model)
    log(f"[{cell}] parameters: {params}")

    optimizer = torch.optim.AdamW(model.parameters(), lr=tcfg["lr"], weight_decay=tcfg["weight_decay"])
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, factor=tcfg["lr_decay"], patience=0)
    ctx, amp_dtype = amp_context(device, cfg)
    scaler = torch.amp.GradScaler("cuda", enabled=amp_dtype == torch.float16)

    history = {"epochs": [], "steps": []}
    best_val, bad_epochs, step = float("inf"), 0, 0
    start = time.time()
    for epoch in range(1, tcfg["epochs"] + 1):
        model.train()
        train_loader.batch_sampler.set_epoch(epoch)
        epoch_start = time.time()
        tok_sum = loss_sum = 0.0
        grad_norms = []
        for inputs, targets, _ in train_loader:
            inputs, targets = inputs.to(device), targets.to(device)
            with ctx:
                logits, _ = model(inputs)
            loss = lm_loss(logits, targets, tokenizer.pad_id)
            optimizer.zero_grad(set_to_none=True)
            scaler.scale(loss).backward()
            scaler.unscale_(optimizer)
            grad_norm = torch.nn.utils.clip_grad_norm_(model.parameters(), tcfg["grad_clip"]).item()
            scaler.step(optimizer)
            scaler.update()

            n_tok = targets.ne(tokenizer.pad_id).sum().item()
            loss_sum += loss.item() * n_tok
            tok_sum += n_tok
            if math.isfinite(grad_norm):
                grad_norms.append(grad_norm)
            step += 1
            if step % tcfg["log_every"] == 0:
                history["steps"].append({"step": step, "epoch": epoch, "train_loss": loss.item(),
                                         "grad_norm": grad_norm})

        train_loss = loss_sum / tok_sum
        val = evaluate(model, val_loader, tokenizer.pad_id, device, cfg)
        scheduler.step(val["loss"])
        record = {
            "epoch": epoch, "train_loss": train_loss, "train_ppl": math.exp(train_loss),
            "val_loss": val["loss"], "val_ppl": val["ppl"], "lr": optimizer.param_groups[0]["lr"],
            "grad_norm_mean": float(np.mean(grad_norms)), "grad_norm_max": float(np.max(grad_norms)),
            "epoch_seconds": time.time() - epoch_start,
        }
        history["epochs"].append(record)
        log(f"[{cell}] epoch {epoch:2d} train_loss {train_loss:.4f} val_loss {val['loss']:.4f} "
            f"val_ppl {val['ppl']:.2f} grad_norm {record['grad_norm_mean']:.2f} "
            f"lr {record['lr']:.2e} ({record['epoch_seconds']:.0f}s)")

        if val["loss"] < best_val - 1e-4:
            best_val, bad_epochs = val["loss"], 0
            torch.save({"cell": cell, "state_dict": model.state_dict(), "epoch": epoch,
                        "val_loss": val["loss"], "model_cfg": cfg["model"]}, ckpt_path)
        else:
            bad_epochs += 1
            if bad_epochs >= tcfg["patience"]:
                log(f"[{cell}] early stopping after epoch {epoch}")
                break

    summary = {
        "cell": cell, "parameters": params, "train_seconds": time.time() - start,
        "epochs_run": len(history["epochs"]),
        "best_epoch": min(history["epochs"], key=lambda r: r["val_loss"])["epoch"],
        "best_val_loss": best_val, "best_val_ppl": math.exp(best_val),
        "amp_dtype": str(amp_dtype), "finished": timestamp(), "hardware": hardware_info(),
        "train_cfg": tcfg, "model_cfg": cfg["model"], "seed": cfg["seed"],
    }
    return history, summary


def load_model(ckpt_path, cfg, tokenizer, device):
    ckpt = torch.load(ckpt_path, map_location=device, weights_only=True)
    model = build_model(ckpt["cell"], cfg, len(tokenizer), tokenizer.pad_id).to(device)
    model.load_state_dict(ckpt["state_dict"])
    model.eval()
    return model, ckpt
