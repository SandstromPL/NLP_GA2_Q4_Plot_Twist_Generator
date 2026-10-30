"""Decoding strategies: greedy, temperature sampling, top-k, top-p, optional repetition penalty."""
import torch

from .tokenizer import detokenize


def apply_repetition_penalty(logits, previous_ids, penalty):
    """CTRL-style penalty (Keskar et al., 2019): shrink the logits of tokens already in the text."""
    if penalty == 1.0 or not previous_ids:
        return logits
    idx = torch.tensor(sorted(set(previous_ids)), device=logits.device)
    vals = logits[idx]
    logits[idx] = torch.where(vals > 0, vals / penalty, vals * penalty)
    return logits


def next_token(logits, dcfg, generator):
    """Pick one id from a 1-D logits vector according to the decoding config."""
    if dcfg["strategy"] == "greedy":
        return int(torch.argmax(logits))
    logits = logits / dcfg.get("temperature", 1.0)
    top_k = dcfg.get("top_k")
    if top_k:
        kth = torch.topk(logits, top_k).values[-1]
        logits = logits.masked_fill(logits < kth, float("-inf"))
    top_p = dcfg.get("top_p")
    if top_p:
        sorted_logits, order = torch.sort(logits, descending=True)
        cum = torch.softmax(sorted_logits, dim=-1).cumsum(-1)
        remove = cum - torch.softmax(sorted_logits, dim=-1) > top_p  # keep the token that crosses top_p
        logits = logits.clone()
        logits[order[remove]] = float("-inf")
    probs = torch.softmax(logits, dim=-1)
    return int(torch.multinomial(probs, 1, generator=generator))


@torch.no_grad()
def generate(model, tokenizer, prompt, dcfg, seed, max_new_tokens, ban_ids, device):
    """Continue `prompt` token by token. The prompt is never part of the returned continuation."""
    model.eval()
    generator = torch.Generator().manual_seed(seed)  # sampling runs on CPU for reproducibility
    prompt_ids = tokenizer.encode(prompt, add_bos=True)
    logits, hidden = model(torch.tensor([prompt_ids], device=device))
    step_logits = logits[0, -1]
    out_ids, stop_reason = [], "max_len"
    for _ in range(max_new_tokens):
        scores = step_logits.float().cpu().clone()
        scores[ban_ids] = float("-inf")
        scores = apply_repetition_penalty(scores, prompt_ids[1:] + out_ids, dcfg.get("repetition_penalty", 1.0))
        tok = next_token(scores, dcfg, generator)
        if tok == tokenizer.eos_id:
            stop_reason = "eos"
            break
        out_ids.append(tok)
        logits, hidden = model(torch.tensor([[tok]], device=device), hidden)
        step_logits = logits[0, -1]
    tokens = tokenizer.decode_tokens(out_ids)
    return {
        "prompt_tokens": tokenizer.decode_tokens(prompt_ids[1:]),
        "prompt_oov": tokenizer.oov_words(prompt),
        "tokens": tokens,
        "text": detokenize(tokens),
        "n_tokens": len(tokens),
        "stop_reason": stop_reason,
    }


def run_generation_grid(models, tokenizer, prompts, cfg, device, log=print):
    """Every model x prompt x decoding config x seed (greedy configs use a single seed)."""
    gcfg = cfg["generation"]
    ban_ids = [tokenizer.stoi[t] for t in gcfg["ban_tokens"]]
    rows = []
    for model_name, model in models.items():
        for prompt in prompts:
            for dcfg in gcfg["configs"]:
                seeds = gcfg["seeds"][:1] if dcfg["strategy"] == "greedy" else gcfg["seeds"]
                for seed in seeds:
                    res = generate(model, tokenizer, prompt["text"], dcfg, seed, gcfg["max_new_tokens"],
                                   ban_ids, device)
                    rows.append({"system": model_name, "prompt_id": prompt["id"], "group": prompt["group"],
                                 "prompt": prompt["text"], "config": dcfg["name"], "decoding": dcfg,
                                 "seed": seed, "max_new_tokens": gcfg["max_new_tokens"], **res})
        log(f"generated {sum(r['system'] == model_name for r in rows)} continuations for {model_name}")
    return rows


def run_length_test(models, tokenizer, test_rows, cfg, device, log=print):
    """Termination check on held-out stories: start from each test story's first sentence and let
    the model write until <eos> or a generous cap, then compare with the story's real remaining length."""
    lcfg, gcfg = cfg["length_test"], cfg["generation"]
    ban_ids = [tokenizer.stoi[t] for t in gcfg["ban_tokens"]]
    configs = [c for c in gcfg["configs"] if c["name"] in lcfg["configs"]]
    rows = []
    for story in test_rows[: lcfg["n_stories"]]:
        text = story["text"]
        cut = min((i for i in (text.find(". "), text.find("! "), text.find("? ")) if i > 0), default=-1)
        if cut < 0:
            continue
        prompt = text[: cut + 1]
        true_rest = len(tokenizer.tokenize(text[cut + 1:]))
        for name, model in models.items():
            for dcfg in configs:
                res = generate(model, tokenizer, prompt, dcfg, lcfg["seed"], lcfg["max_new_tokens"], ban_ids, device)
                rows.append({"system": name, "hf_index": story["hf_index"], "config": dcfg["name"],
                             "n_tokens": res["n_tokens"], "stop_reason": res["stop_reason"], "true_rest": true_rest})
    log(f"length test: {len(rows)} generations")
    return rows
