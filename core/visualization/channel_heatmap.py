from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

def plot_channel_time_heatmap(x: np.ndarray, title: str = "Channel–time heatmap") -> None:
    """Quick-look heatmap for data with shape (n_samples, n_channels)."""
    plt.figure()
    plt.imshow(x.T, aspect="auto", origin="lower")
    plt.title(title)
    plt.xlabel("Time sample")
    plt.ylabel("Channel")
    plt.tight_layout()
