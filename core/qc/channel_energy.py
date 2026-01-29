from __future__ import annotations

import numpy as np

def rms_per_channel(x: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    """Compute RMS per channel (axis=0 time)."""
    return np.sqrt(np.mean(np.square(x), axis=0) + eps)
