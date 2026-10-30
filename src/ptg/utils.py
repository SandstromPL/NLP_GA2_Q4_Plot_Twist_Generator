"""Shared helpers: config loading, seeding, IO and run metadata."""
import json
import os
import platform
import random
import time
from pathlib import Path

import numpy as np
import torch
import yaml


def load_config(path="configs/default.yaml", overrides=None):
    with open(path) as f:
        cfg = yaml.safe_load(f)
    for dotted, value in (overrides or {}).items():
        node = cfg
        *parents, leaf = dotted.split(".")
        for key in parents:
            node = node[key]
        node[leaf] = value
    return cfg


def out_path(cfg, *parts):
    path = Path(cfg["output_dir"], *parts)
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def get_device():
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def hardware_info():
    info = {
        "python": platform.python_version(),
        "torch": torch.__version__,
        "platform": platform.platform(),
        "cpu_count": os.cpu_count(),
        "device": "cpu",
    }
    if torch.cuda.is_available():
        props = torch.cuda.get_device_properties(0)
        info.update(device=props.name, gpu_memory_gb=round(props.total_memory / 2**30, 2),
                    cuda=torch.version.cuda, cudnn=torch.backends.cudnn.version())
    return info


def save_json(obj, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(obj, f, indent=2)


def load_json(path):
    with open(path) as f:
        return json.load(f)


def save_jsonl(rows, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        for row in rows:
            f.write(json.dumps(row) + "\n")


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S")
