from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class SensorMetadata:
    sampling_rate_hz: float
    units: str = "arb"
    channel_labels: Optional[list[str]] = None
    notes: str = ""

# Extend: geometry, gauge length, calibration, timestamps, etc.
