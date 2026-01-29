import numpy as np
from core.qc.channel_energy import rms_per_channel

def test_rms_shape():
    x = np.zeros((100, 5), dtype=float)
    y = rms_per_channel(x)
    assert y.shape == (5,)
