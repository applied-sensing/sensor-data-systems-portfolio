from __future__ import annotations

import numpy as np

def robust_zscore(x: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    """Robust per-channel z-score using median and MAD (axis=0 time)."""
    med = np.median(x, axis=0, keepdims=True)
    mad = np.median(np.abs(x - med), axis=0, keepdims=True) + eps
    return (x - med) / (1.4826 * mad)
