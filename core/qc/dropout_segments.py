from __future__ import annotations

import numpy as np
from dataclasses import dataclass

@dataclass(frozen=True)
class DropoutSegment:
    channel: int
    start: int
    end: int  # exclusive
    length: int

def find_zero_dropouts(x: np.ndarray, min_len: int = 10) -> list[DropoutSegment]:
    """Find contiguous zero-valued dropout segments per channel."""
    segments: list[DropoutSegment] = []
    n_samples, n_ch = x.shape
    for ch in range(n_ch):
        z = (x[:, ch] == 0)
        if not np.any(z):
            continue
        idx = np.flatnonzero(np.diff(np.concatenate(([0], z.view(np.int8), [0]))))
        starts = idx[0::2]
        ends = idx[1::2]
        for s, e in zip(starts, ends):
            L = int(e - s)
            if L >= min_len:
                segments.append(DropoutSegment(channel=int(ch), start=int(s), end=int(e), length=L))
    return segments
