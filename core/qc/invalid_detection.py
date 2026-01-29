from __future__ import annotations

import numpy as np

def nan_fraction_per_channel(x: np.ndarray) -> np.ndarray:
    """Return per-channel fraction of NaNs (axis=0 time)."""
    return np.mean(np.isnan(x), axis=0)

def invalid_channels_by_nan_fraction(x: np.ndarray, max_nan_fraction: float) -> np.ndarray:
    """Flag channels with NaN fraction >= max_nan_fraction."""
    frac_nan = nan_fraction_per_channel(x)
    return frac_nan >= max_nan_fraction
