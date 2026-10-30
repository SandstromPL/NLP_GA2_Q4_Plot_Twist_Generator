"""Builds notebooks/Q4_Plot_Twist_Generator.ipynb (run from the project root, then execute it with
`jupyter nbconvert --to notebook --execute --inplace notebooks/Q4_Plot_Twist_Generator.ipynb`)."""
import nbformat as nbf

cells = []
md = lambda s: cells.append(nbf.v4.new_markdown_cell(s.strip()))
code = lambda s: cells.append(nbf.v4.new_code_cell(s.strip()))

md("""
# Plot-Twist Generator: Vanilla RNN vs LSTM on TinyStories
NLP Group Assignment 2, Question 4.

This notebook walks through the experiment **using the saved outputs** of the pipeline
(`python -m ptg.cli all`, see README). Heavy steps (training, generation) run as scripts; this
notebook loads their results, shows every table and figure, and ends with a live generation demo.

Convention: text in `> quote` blocks or printed under **MODEL OUTPUT** is machine-generated and
unedited. Everything else is human-written commentary.
""")
code("""
import os, sys, json
from pathlib import Path
ROOT = Path.cwd() if (Path.cwd() / "configs").exists() else Path.cwd().parent
os.chdir(ROOT); sys.path.insert(0, str(ROOT / "src"))
import pandas as pd, torch
from IPython.display import Image, Markdown, display
from ptg.utils import load_config, load_json, load_jsonl
from ptg.tokenizer import WordTokenizer
cfg = load_config("configs/default.yaml")
OUT = Path(cfg["output_dir"])
pd.set_option("display.max_colwidth", 200, "display.width", 200)
print("seed:", cfg["seed"])
""")

md("## Part 1: Dataset preparation and next-token examples")
code("""
stats = load_json(OUT / "data_stats.json")
print(json.dumps(stats["splits"], indent=1))
print(json.dumps(stats["vocab"], indent=1))
pd.DataFrame({k: {kk: vv for kk, vv in v.items() if kk != "story_length_tokens"} for k, v in stats["sequences"].items()})
""")
code("""display(Image(OUT / "figures/story_lengths.png"))""")
code("""print((OUT / "examples/input_target_pairs.txt").read_text())""")
md("""
**Padding demo.** A batch of two windows of different length is right-padded with `<pad>`=0.
Targets at padded positions are 0 and the loss ignores them (`ignore_index=0`). The models read
left to right, so the padding after a sequence cannot change any prediction made before it.
""")
code("""
from ptg.dataset import StoryLMDataset, make_collate
tok = WordTokenizer.load(OUT / "vocab.json")
ds = StoryLMDataset(["Tom saw a dog.", "Lily had a red ball and she liked it."], tok, cfg["sequences"]["max_len"])
x, y, offsets = make_collate(tok.pad_id)([ds[0], ds[1]])
print("inputs :\\n", x); print("targets:\\n", y)
print("tokens counted by the loss:", int(y.ne(tok.pad_id).sum()), "of", y.numel())
""")
code("""
print("Prompt words outside the vocabulary (they become <unk>):")
for pid, words in stats["prompt_oov"].items():
    print(f"  {pid:22s} {words}")
""")

md("## Part 2: Vanilla RNN and LSTM language models")
code("""
from ptg.models import build_model, count_parameters
for cell in ("rnn", "lstm"):
    m = build_model(cell, cfg, len(tok), tok.pad_id)
    print(m); print(count_parameters(m), "\\n")
""")
code("""
pd.read_csv(OUT / "tables/model_summary.csv")
""")
code("""display(Image(OUT / "figures/loss_curves.png")); display(Image(OUT / "figures/train_loss_steps.png"))""")
code("""
for cell in ("rnn", "lstm"):
    h = load_json(OUT / f"training/{cell}_history.json")
    print(cell); display(pd.DataFrame(h["epochs"]).round(4))
""")
code("""display(Image(OUT / "figures/grad_norms.png"))""")
md("""
**Loss by position in the story.** If a model uses long context well, its loss should keep
falling as it reads further into a story.
""")
code("""display(Image(OUT / "figures/loss_by_position.png"))""")

md("## Part 3: Decoding strategies")
code("""
settings = load_json(OUT / "generations/generation_settings.json")
pd.DataFrame(settings["generation"]["configs"])
""")
code("""
dec = pd.read_csv(OUT / "tables/decoding_metrics.csv")
dec[dec.system != "llm"].round(3)
""")
code("""display(Image(OUT / "figures/temperature_effect.png")); display(Image(OUT / "figures/diversity_vs_repetition.png"))""")
code("""
gens = load_jsonl(OUT / "generations/generations.jsonl")
def show(prompt_id, configs, systems=("rnn", "lstm"), seed=0):
    rows = [r for r in gens if r["prompt_id"] == prompt_id]
    display(Markdown(f"**Opening (human-written):** {rows[0]['prompt']}"))
    for system in systems:
        for c in configs:
            r = next(r for r in rows if r["system"] == system and r["config"] == c and r["seed"] == seed)
            display(Markdown(f"**MODEL OUTPUT: {system} / {c} / seed {seed}** ({r['n_tokens']} tokens, stop={r['stop_reason']})\\n\\n> {r['text'] or '(empty)'}"))
show("P3_mystery", ["greedy", "temp_0.5", "temp_0.8", "temp_1.2", "topk_40"])
""")
code("""show("P3_problem", ["greedy", "temp_0.8", "temp_1.2", "topk_10", "topk_40_rep1.2"])""")
md("All generations for all Part 3 prompts: `outputs/stories/part3_stories.md`.")
md("""
**Termination on held-out stories.** On the creative prompts many samples hit the 150-token cap,
but real stories are longer than that. So we start from the first sentence of 100 *test*
stories, allow up to 600 tokens, and compare with the real remaining length.
""")
code("""pd.read_csv(OUT / "tables/length_test.csv").round(1)""")
md("**Automatic failure flags** (% of samples): loops, runaway, premature, off-prompt, stock characters.")
code("""dec[["system", "config", "loop_pct", "runaway_pct", "premature_pct", "off_prompt_pct", "stock_character_pct"]].round(0)""")

md("## Part 4: The Plot-Twist Challenge")
code("""
for pid in ["P4_exam", "P4_robot", "P4_detective", "P4_village", "P4_letter"]:
    show(pid, ["greedy", "temp_0.8", "topk_40"])
""")
code("""pd.read_csv(OUT / "tables/plot_twist_metrics.csv").round(3)""")
md("All Part 4 generations (5 seeds × 10 configs × 2 models + LLM): `outputs/stories/part4_stories.md`.")
md("""
**Criteria judgements (analyst annotation, human-written).** Each seed-0 continuation (greedy, T=0.8,
top-k=40) is judged on the four criteria of the brief: Yes / Partial / No, with a reason.
""")
code("""
crit = pd.read_csv(OUT / "analysis/part4_criteria.csv")
score = {"Yes": 1, "Partial": 0.5, "No": 0}
cols = ["connected", "twist", "consistent", "no_repetition"]
display(crit.assign(**{c: crit[c].map(score) for c in cols}).groupby(["system", "config"], sort=False)[cols].mean())
crit[["prompt_id", "system", "config"] + cols + ["note"]]
""")
md("""
**Does the prompt or the random seed decide the story?** Continuations of *different* prompts with
the *same* seed are compared with continuations of the *same* prompt with *different* seeds.
""")
code("""pd.read_csv(OUT / "tables/prompt_sensitivity.csv").round(3)""")

md("## Part 5: Quantitative and human evaluation")
code("""
ppl = load_json(OUT / "eval/perplexity.json")
pd.DataFrame({c: {"val_ppl": ppl[c]["val"]["ppl"], "test_ppl": ppl[c]["test"]["ppl"]} for c in ("rnn", "lstm")}).T.round(2)
""")
code("""pd.read_csv(OUT / "tables/system_metrics_all_configs.csv").round(3)""")
code("""
hdir = OUT / "human_eval"
done = [p for p in (hdir / "ratings").glob("*.csv") if p.stem != "TEMPLATE"]
if (hdir / "results_by_system.csv").exists():
    for name in ["by_system", "by_config", "agreement", "lstm_vs_rnn", "metric_vs_human", "disagreements"]:
        f = hdir / f"results_{name}.csv"
        if f.exists():
            print(name); display(pd.read_csv(f).round(3).head(12))
else:
    print(f"Human ratings not analysed yet ({len(done)} rating files found). Run: python -m ptg.cli human-analyze")
""")

md("## Optional extension: Qwen2.5-0.5B-Instruct (zero-shot)")
code("""
llm_path = OUT / "generations/llm_generations.jsonl"
if llm_path.exists():
    meta = load_json(OUT / "generations/llm_settings.json")
    print(json.dumps({k: v for k, v in meta.items() if k != "hardware"}, indent=1))
    llm = load_jsonl(llm_path)
    for r in [r for r in llm if r["config"] == "topk_40" and r["seed"] == 0]:
        display(Markdown(f"**{r['prompt_id']}: MODEL OUTPUT (Qwen, topk_40, seed 0)**\\n\\n> {r['text']}"))
    display(dec[dec.system == "llm"].round(3))
""")

md("""
## Live demo: the Plot-Twist Generator
Type any opening and pick a decoding config. The models were trained only on TinyStories, so
words outside their 7.6k-word vocabulary become `<unk>`.
""")
code("""
from ptg.train import load_model
from ptg.generate import generate
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
models = {c: load_model(OUT / f"checkpoints/{c}.pt", cfg, tok, device)[0] for c in ("rnn", "lstm")}
ban = [tok.stoi[t] for t in cfg["generation"]["ban_tokens"]]
configs = {c["name"]: c for c in cfg["generation"]["configs"]}

def plot_twist(opening, config="topk_40", seed=0):
    display(Markdown(f"**Opening (human-written):** {opening}"))
    for name, model in models.items():
        r = generate(model, tok, opening, configs[config], seed, cfg["generation"]["max_new_tokens"], ban, device)
        display(Markdown(f"**MODEL OUTPUT: {name} / {config} / seed {seed}**\\n\\n> {r['text']}"))

plot_twist("One day, a little girl found a door in the tree behind her house. When she opened it,")
""")

nb = nbf.v4.new_notebook(cells=cells, metadata={"kernelspec": {"name": "python3", "display_name": "Python 3",
                                                               "language": "python"}})
nbf.write(nb, "notebooks/Q4_Plot_Twist_Generator.ipynb")
print("wrote notebooks/Q4_Plot_Twist_Generator.ipynb")
