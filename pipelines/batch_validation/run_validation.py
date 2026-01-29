from __future__ import annotations

import argparse
from pathlib import Path
import json

import numpy as np
import yaml

from core.io.numpy_io import load_npy
from core.qc.channel_energy import rms_per_channel
from core.qc.dropout_detection import fraction_zeros_per_channel
from core.utils.logging import info

def main() -> None:
    p = argparse.ArgumentParser(description="Batch validation scaffold (QC metrics + JSON report).")
    p.add_argument("--config", type=str, default=str(Path(__file__).with_name("config.yaml")))
    args = p.parse_args()

    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    x = load_npy(cfg["data"]["path"])

    metrics: dict[str, list[float]] = {}
    if cfg["qc"].get("rms", False):
        metrics["rms_per_channel"] = rms_per_channel(x).astype(float).tolist()
    if cfg["qc"].get("fraction_zeros", False):
        metrics["fraction_zeros_per_channel"] = fraction_zeros_per_channel(x).astype(float).tolist()

    out_dir = Path(cfg["output"]["out_dir"])
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "qc_metrics.json"
    out_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    info(f"Wrote metrics to: {out_path}")

if __name__ == "__main__":
    main()
