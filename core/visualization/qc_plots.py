from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def save_rms_bar(rms: np.ndarray, out_path: str | Path, title: str = "RMS per channel") -> None:
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.figure()
    plt.bar(np.arange(rms.size), rms)
    plt.title(title)
    plt.xlabel("Channel")
    plt.ylabel("RMS")
    plt.tight_layout()
    plt.savefig(out_path, dpi=180)
    plt.close()

def save_channel_time_heatmap(
    x: np.ndarray,
    out_path: str | Path,
    title: str = "Channel–time heatmap",
    max_channels: int | None = None,
) -> None:
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    x2 = x[:, :max_channels] if (max_channels is not None and x.shape[1] > max_channels) else x
    plt.figure()
    plt.imshow(x2.T, aspect="auto", origin="lower")
    plt.title(title)
    plt.xlabel("Time sample")
    plt.ylabel("Channel")
    plt.tight_layout()
    plt.savefig(out_path, dpi=180)
    plt.close()
