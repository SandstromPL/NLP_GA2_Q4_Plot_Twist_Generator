"""Model A: Embedding -> Vanilla RNN -> Linear.  Model B: Embedding -> LSTM -> Linear."""
import torch.nn as nn


class RecurrentLM(nn.Module):
    def __init__(self, cell, vocab_size, emb_dim, hidden_dim, num_layers, dropout, pad_id):
        super().__init__()
        if cell not in ("rnn", "lstm"):
            raise ValueError(f"cell must be 'rnn' or 'lstm', got {cell!r}")
        self.cell = cell
        self.embedding = nn.Embedding(vocab_size, emb_dim, padding_idx=pad_id)
        recurrent = dict(input_size=emb_dim, hidden_size=hidden_dim, num_layers=num_layers,
                         batch_first=True, dropout=dropout if num_layers > 1 else 0.0)
        self.rnn = nn.RNN(nonlinearity="tanh", **recurrent) if cell == "rnn" else nn.LSTM(**recurrent)
        self.drop = nn.Dropout(dropout)
        self.fc = nn.Linear(hidden_dim, vocab_size)

    def forward(self, input_ids, hidden=None):
        """input_ids: (batch, time) -> logits (batch, time, vocab), final hidden state."""
        out, hidden = self.rnn(self.drop(self.embedding(input_ids)), hidden)
        return self.fc(self.drop(out)), hidden


def build_model(cell, cfg, vocab_size, pad_id):
    m = cfg["model"]
    return RecurrentLM(cell, vocab_size, m["emb_dim"], m["hidden_dim"], m["num_layers"], m["dropout"], pad_id)


def count_parameters(model):
    groups = {"embedding": model.embedding, "recurrent": model.rnn, "output": model.fc}
    counts = {name: sum(p.numel() for p in mod.parameters()) for name, mod in groups.items()}
    counts["total"] = sum(p.numel() for p in model.parameters())
    return counts
