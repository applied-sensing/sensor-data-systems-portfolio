from __future__ import annotations

import numpy as np
from pathlib import Path
from typing import Any

def load_npy(path: str | Path) -> np.ndarray:
    """Load a numpy array (e.g., shape (n_samples, n_channels))."""
    return np.load(Path(path))

def save_npy(path: str | Path, arr: np.ndarray) -> None:
    """Save a numpy array."""
    np.save(Path(path), arr)

def load_metadata_json(path: str | Path) -> dict[str, Any]:
    """Placeholder for metadata I/O (extend as needed)."""
    import json
    return json.loads(Path(path).read_text(encoding="utf-8"))
