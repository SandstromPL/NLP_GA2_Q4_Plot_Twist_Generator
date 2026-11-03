"""Continue any story opening with the trained models:

    python -m ptg.demo "One day, a little girl found a door in a tree." [--decoding topk_40] [--seed 0]

Uses outputs/vocab.json and outputs/checkpoints/{rnn,lstm}.pt. Nothing is written to outputs/;
the continuations are only printed.
"""
import argparse

from .generate import generate
from .tokenizer import WordTokenizer
from .train import load_model
from .utils import get_device, load_config, out_path


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("opening", help="story opening to continue")
    parser.add_argument("--config", default="configs/default.yaml")
    parser.add_argument("--model", default="both", choices=["rnn", "lstm", "both"])
    parser.add_argument("--decoding", default="topk_40", help="decoding config name from generation.configs")
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--max-new-tokens", type=int, help="default: generation.max_new_tokens")
    args = parser.parse_args(argv)

    cfg = load_config(args.config)
    gcfg = cfg["generation"]
    configs = {c["name"]: c for c in gcfg["configs"]}
    if args.decoding not in configs:
        parser.error(f"unknown --decoding {args.decoding!r}; choose from: {', '.join(configs)}")
    device = get_device()
    tok = WordTokenizer.load(out_path(cfg, "vocab.json"))
    ban_ids = [tok.stoi[t] for t in gcfg["ban_tokens"]]
    cells = ("rnn", "lstm") if args.model == "both" else (args.model,)

    print(f"Opening: {args.opening}")
    oov = tok.oov_words(args.opening)
    if oov:
        print(f"Not in the vocabulary (read as <unk>): {', '.join(oov)}")
    for cell in cells:
        model = load_model(out_path(cfg, "checkpoints", f"{cell}.pt"), cfg, tok, device)[0]
        r = generate(model, tok, args.opening, configs[args.decoding], args.seed,
                     args.max_new_tokens or gcfg["max_new_tokens"], ban_ids, device)
        print(f"\n--- {cell.upper()} | {args.decoding} | seed {args.seed} | {r['n_tokens']} tokens, "
              f"stopped by {r['stop_reason']} ---\n{r['text']}")


if __name__ == "__main__":
    main()
