from __future__ import annotations

import numpy as np

def dead_channels_by_rms(x: np.ndarray, min_rms: float, eps: float = 1e-12) -> np.ndarray:
    """Flag channels whose RMS is below `min_rms` (axis=0 time)."""
    rms = np.sqrt(np.mean(np.square(x), axis=0) + eps)
    return rms < min_rms

def dead_channels_by_zero_fraction(x: np.ndarray, max_zero_fraction: float = 0.95) -> np.ndarray:
    """Flag channels with a high fraction of exact zeros."""
    frac0 = np.mean(x == 0, axis=0)
    return frac0 >= max_zero_fraction
