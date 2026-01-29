from __future__ import annotations

import numpy as np
from scipy.signal import butter, filtfilt

def bandpass(x: np.ndarray, fs_hz: float, low_hz: float, high_hz: float, order: int = 4) -> np.ndarray:
    """Bandpass filter along time axis (axis=0)."""
    nyq = 0.5 * fs_hz
    b, a = butter(order, [low_hz/nyq, high_hz/nyq], btype="band")
    return filtfilt(b, a, x, axis=0)
