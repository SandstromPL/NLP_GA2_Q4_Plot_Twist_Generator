"""Next-token training examples: one sequence per story, never crossing story boundaries."""
import random

import torch
from torch.utils.data import Dataset, Sampler


def story_windows(ids, max_len):
    """Split one encoded story (<bos> ... <eos>) into (input, target, offset) windows.

    A story of up to max_len + 1 ids gives one window. Longer stories are cut into consecutive
    windows of the *same* story that overlap by one id, so every target id is predicted exactly once.
    """
    windows = []
    for start in range(0, max(len(ids) - 1, 1), max_len):
        chunk = ids[start: start + max_len + 1]
        if len(chunk) >= 2:
            windows.append((chunk[:-1], chunk[1:], start))
    return windows


class StoryLMDataset(Dataset):
    def __init__(self, texts, tokenizer, max_len):
        self.items, self.n_split_stories = [], 0
        for text in texts:
            ids = tokenizer.encode(text, add_bos=True, add_eos=True)
            wins = story_windows(ids, max_len)
            self.n_split_stories += len(wins) > 1
            self.items.extend(wins)
        self.n_stories = len(texts)
        self.n_target_tokens = sum(len(t) for _, t, _ in self.items)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, i):
        return self.items[i]


class TokenBudgetSampler(Sampler):
    """Groups windows of similar length so a batch holds about max_tokens tokens (less padding)."""

    def __init__(self, lengths, max_tokens, shuffle, seed=0):
        self.lengths, self.max_tokens, self.shuffle, self.seed = lengths, max_tokens, shuffle, seed
        self.epoch = 0
        self.batches = self._make_batches()

    def set_epoch(self, epoch):
        self.epoch = epoch
        self.batches = self._make_batches()

    def _make_batches(self):
        rng = random.Random(self.seed + self.epoch)
        order = list(range(len(self.lengths)))
        if self.shuffle:
            rng.shuffle(order)
        # Sort inside large chunks only, so batches differ between epochs but stay length-homogeneous.
        chunk = 100 * 64
        order = [i for s in range(0, len(order), chunk)
                 for i in sorted(order[s: s + chunk], key=lambda j: self.lengths[j])]
        batches, cur, cur_max = [], [], 0
        for i in order:
            new_max = max(cur_max, self.lengths[i])
            if cur and new_max * (len(cur) + 1) > self.max_tokens:
                batches.append(cur)
                cur, new_max = [], self.lengths[i]
            cur.append(i)
            cur_max = new_max
        if cur:
            batches.append(cur)
        if self.shuffle:
            rng.shuffle(batches)
        return batches

    def __iter__(self):
        return iter(self.batches)

    def __len__(self):
        return len(self.batches)


def make_collate(pad_id):
    """Right-pad to the longest window in the batch. Padded targets use pad_id and are ignored by
    the loss (ignore_index); because the models are causal, right padding cannot change the
    hidden states or predictions at real positions."""

    def collate(batch):
        max_len = max(len(x) for x, _, _ in batch)
        inputs = torch.full((len(batch), max_len), pad_id, dtype=torch.long)
        targets = torch.full((len(batch), max_len), pad_id, dtype=torch.long)
        offsets = torch.tensor([off for _, _, off in batch], dtype=torch.long)
        for row, (x, y, _) in enumerate(batch):
            inputs[row, : len(x)] = torch.tensor(x)
            targets[row, : len(y)] = torch.tensor(y)
        return inputs, targets, offsets

    return collate


def make_loader(dataset, pad_id, max_tokens, shuffle, seed=0):
    from torch.utils.data import DataLoader

    lengths = [len(x) for x, _, _ in dataset.items]
    sampler = TokenBudgetSampler(lengths, max_tokens, shuffle, seed)
    return DataLoader(dataset, batch_sampler=sampler, collate_fn=make_collate(pad_id), num_workers=0)
