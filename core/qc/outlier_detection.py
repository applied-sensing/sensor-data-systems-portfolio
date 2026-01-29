from __future__ import annotations

import numpy as np

def robust_channel_outliers(values: np.ndarray, z_thresh: float = 4.0, eps: float = 1e-12) -> np.ndarray:
    """Robust outlier flagging for per-channel scalars using median/MAD."""
    med = np.median(values)
    mad = np.median(np.abs(values - med)) + eps
    z = (values - med) / (1.4826 * mad)
    return np.abs(z) >= z_thresh
