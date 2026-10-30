"""Word-level tokenizer shared by both models (same procedure, same vocabulary)."""
import re
from collections import Counter

from .utils import load_json, save_json

PAD, UNK, BOS, EOS = "<pad>", "<unk>", "<bos>", "<eos>"
SPECIALS = [PAD, UNK, BOS, EOS]

# Words, clitics ('s, 't, 'll ...), numbers, and every other non-space character as its own token.
TOKEN_RE = re.compile(r"[a-z]+|'[a-z]+|\d+|[^\sa-z\d]", re.IGNORECASE)
NO_SPACE_BEFORE = set(".,!?;:)%")
NO_SPACE_AFTER = set("($")


def is_word(token):
    return token[0].isalpha() or (token[0] == "'" and len(token) > 1)


class WordTokenizer:
    def __init__(self, itos, lowercase=True):
        self.itos = list(itos)
        self.stoi = {tok: i for i, tok in enumerate(self.itos)}
        self.lowercase = lowercase
        self.pad_id, self.unk_id, self.bos_id, self.eos_id = (self.stoi[t] for t in SPECIALS)

    def __len__(self):
        return len(self.itos)

    # ---- building / saving -------------------------------------------------------------
    @classmethod
    def build(cls, texts, min_freq, max_vocab, lowercase=True):
        counts = Counter()
        for text in texts:
            counts.update(cls.split(text, lowercase))
        ranked = sorted((tok for tok, c in counts.items() if c >= min_freq), key=lambda t: (-counts[t], t))
        itos = SPECIALS + ranked[: max_vocab - len(SPECIALS)]
        tok = cls(itos, lowercase)
        stats = {
            "train_types": len(counts),
            "train_tokens": sum(counts.values()),
            "vocab_size": len(itos),
            "min_freq": min_freq,
            "train_tokens_covered": sum(counts[t] for t in itos if t in counts) / sum(counts.values()),
        }
        return tok, stats

    def save(self, path):
        save_json({"itos": self.itos, "lowercase": self.lowercase}, path)

    @classmethod
    def load(cls, path):
        obj = load_json(path)
        return cls(obj["itos"], obj["lowercase"])

    # ---- text <-> tokens <-> ids ----------------------------------------------------------
    @staticmethod
    def split(text, lowercase=True):
        if lowercase:
            text = text.lower()
        return TOKEN_RE.findall(text)

    def tokenize(self, text):
        return self.split(text, self.lowercase)

    def encode(self, text, add_bos=False, add_eos=False):
        ids = [self.stoi.get(tok, self.unk_id) for tok in self.tokenize(text)]
        return ([self.bos_id] if add_bos else []) + ids + ([self.eos_id] if add_eos else [])

    def decode_tokens(self, ids):
        return [self.itos[i] for i in ids]

    def oov_words(self, text):
        return [tok for tok in self.tokenize(text) if tok not in self.stoi]

    def unk_rate(self, texts):
        total = unk = 0
        for text in texts:
            toks = self.tokenize(text)
            total += len(toks)
            unk += sum(tok not in self.stoi for tok in toks)
        return unk / max(total, 1)


def detokenize(tokens, capitalize=True):
    """Join word tokens into readable text. Used identically for every system shown to evaluators."""
    out, quote_open, glue_next = "", False, True
    for tok in tokens:
        if tok in (BOS, EOS, PAD):
            continue
        if tok == '"':
            if quote_open:
                out += tok
            else:
                out += ("" if glue_next else " ") + tok
                glue_next = True
                quote_open = not quote_open
                continue
            quote_open = not quote_open
            glue_next = False
            continue
        attach = glue_next or tok in NO_SPACE_BEFORE or (tok.startswith("'") and len(tok) > 1)
        out += ("" if attach else " ") + tok
        glue_next = tok in NO_SPACE_AFTER
    out = out.strip()
    if capitalize:
        out = re.sub(r"(^|[.!?]\s+\"?|^\")([a-z])", lambda m: m.group(1) + m.group(2).upper(), out)
        out = re.sub(r"\bi\b", "I", out)
    return out
