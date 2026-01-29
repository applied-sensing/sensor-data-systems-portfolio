from __future__ import annotations

import numpy as np

def sta_lta(x: np.ndarray, sta_samples: int, lta_samples: int, eps: float = 1e-12) -> np.ndarray:
    """Simple STA/LTA ratio per channel; returns array shape (n_samples, n_channels)."""
    # Placeholder implementation (boxcar moving average)
    def movavg(a: np.ndarray, w: int) -> np.ndarray:
        kernel = np.ones(w) / w
        return np.apply_along_axis(lambda v: np.convolve(v, kernel, mode="same"), 0, a)

    absx = np.abs(x)
    sta = movavg(absx, sta_samples)
    lta = movavg(absx, lta_samples)
    return sta / (lta + eps)
