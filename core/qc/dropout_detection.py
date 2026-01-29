from __future__ import annotations

import numpy as np

def fraction_zeros_per_channel(x: np.ndarray) -> np.ndarray:
    """Fraction of exactly-zero samples per channel."""
    return np.mean(x == 0, axis=0)
