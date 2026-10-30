"""Optional baseline: zero-shot open-source LLM (no fine-tuning on TinyStories).

LLM output is re-tokenised with the project's word tokenizer and cut to the same word-token
limit as the RNN/LSTM, so lengths, metrics and the evaluators' view are comparable.
"""
import torch

from .tokenizer import WordTokenizer, detokenize
from .utils import hardware_info


def run_llm(cfg, prompts, word_tok: WordTokenizer, device, log=print):
    from transformers import AutoModelForCausalLM, AutoTokenizer

    lcfg, gcfg = cfg["llm"], cfg["generation"]
    dtype = getattr(torch, lcfg["dtype"]) if device.type == "cuda" else torch.float32
    tok = AutoTokenizer.from_pretrained(lcfg["model_id"])
    model = AutoModelForCausalLM.from_pretrained(lcfg["model_id"], dtype=dtype).to(device).eval()
    eos_ids = model.generation_config.eos_token_id
    eos_ids = set(eos_ids if isinstance(eos_ids, list) else [eos_ids])

    try:
        from huggingface_hub import HfApi
        revision = HfApi().model_info(lcfg["model_id"]).sha
    except Exception as exc:  # metadata only; generation does not depend on it
        revision = f"unavailable ({type(exc).__name__})"

    rows = []
    for prompt in prompts:
        messages = [{"role": "system", "content": lcfg["system_prompt"]},
                    {"role": "user", "content": lcfg["user_template"].format(prompt=prompt["text"])}]
        input_ids = tok.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt",
                                            return_dict=True)["input_ids"].to(device)
        for dcfg in lcfg["configs"]:
            sample = dcfg["strategy"] == "sample"
            seeds = gcfg["seeds"] if sample else gcfg["seeds"][:1]
            for seed in seeds:
                torch.manual_seed(seed)
                # Every decoding knob is set explicitly so the checkpoint's own generation_config
                # (which enables top-p and a repetition penalty) does not leak in.
                gen_kwargs = dict(max_new_tokens=lcfg["max_new_tokens"], do_sample=sample, repetition_penalty=1.0,
                                  temperature=dcfg.get("temperature", 1.0) if sample else None,
                                  top_k=dcfg.get("top_k", 0) if sample else None,
                                  top_p=1.0 if sample else None, pad_token_id=tok.eos_token_id)
                with torch.no_grad():
                    out = model.generate(input_ids, attention_mask=torch.ones_like(input_ids), **gen_kwargs)
                new = out[0, input_ids.shape[1]:].tolist()
                ended = any(t in eos_ids for t in new)
                raw = tok.decode(new, skip_special_tokens=True).strip()
                words = word_tok.tokenize(raw)
                tokens = words[: gcfg["max_new_tokens"]]
                stop_reason = "eos" if ended and len(words) <= gcfg["max_new_tokens"] else "max_len"
                rows.append({
                    "system": "llm", "prompt_id": prompt["id"], "group": prompt["group"], "prompt": prompt["text"],
                    "config": dcfg["name"], "decoding": {**dcfg, "repetition_penalty": 1.0, "top_p": 1.0},
                    "seed": seed, "max_new_tokens": gcfg["max_new_tokens"],
                    "prompt_tokens": word_tok.tokenize(prompt["text"]), "prompt_oov": [],
                    "tokens": tokens, "text": detokenize(tokens), "n_tokens": len(tokens),
                    "stop_reason": stop_reason, "raw_llm_text": raw, "llm_new_subword_tokens": len(new),
                })
        log(f"LLM done: {prompt['id']}")
    meta = {"model_id": lcfg["model_id"], "revision": revision, "dtype": str(dtype),
            "system_prompt": lcfg["system_prompt"], "user_template": lcfg["user_template"],
            "chat_template": "tokenizer.apply_chat_template(add_generation_prompt=True)",
            "max_new_subword_tokens": lcfg["max_new_tokens"], "word_token_cap": gcfg["max_new_tokens"],
            "configs": lcfg["configs"], "seeds": gcfg["seeds"], "fine_tuned": False,
            "hardware": hardware_info()}
    return rows, meta
