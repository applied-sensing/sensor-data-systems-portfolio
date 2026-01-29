from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

import numpy as np
import yaml

from core.io.numpy_io import load_npy
from core.qc.channel_energy import rms_per_channel
from core.qc.dropout_detection import fraction_zeros_per_channel
from core.qc.dead_channel_detection import dead_channels_by_rms, dead_channels_by_zero_fraction
from core.qc.outlier_detection import robust_channel_outliers
from core.qc.dropout_segments import find_zero_dropouts
from core.qc.invalid_detection import nan_fraction_per_channel, invalid_channels_by_nan_fraction
from core.visualization.qc_plots import save_rms_bar, save_channel_time_heatmap
from core.utils.logging import info

def _write_md_report(out_path: Path, payload: dict) -> None:
    dead = payload["flags"]["dead_channels"]
    outliers = payload["flags"]["rms_outliers"]
    segments = payload["dropout_segments"]
    invalid = payload["flags"].get("invalid_channels", [])
    
    lines: list[str] = []
    lines.append("# QC Report — Multichannel baseline\n\n")
    lines.append(f"- Samples: **{payload['shape'][0]}**\n")
    lines.append(f"- Channels: **{payload['shape'][1]}**\n\n")

    lines.append("## Flags\n\n")
    lines.append(f"- Invalid channels (NaN fraction): **{invalid}**\n")
    lines.append(f"- Dead channels (any criterion): **{dead}**\n")
    lines.append(f"- RMS outliers (robust z-score): **{outliers}**\n\n")

    lines.append("## Dropout segments (zero runs)\n\n")
    if len(segments) == 0:
        lines.append("- None detected\n")
    else:
        lines.append("| Channel | Start | End (excl.) | Length |\n|---:|---:|---:|---:|\n")
        for s in segments[:200]:
            lines.append(f"| {s['channel']} | {s['start']} | {s['end']} | {s['length']} |\n")
        if len(segments) > 200:
            lines.append(f"\n... truncated ({len(segments)} total segments)\n")

    out_path.write_text("".join(lines), encoding="utf-8")

def main() -> None:
    ap = argparse.ArgumentParser(description="Project 01: multichannel QC baseline")
    ap.add_argument("--config", type=str, default=str(Path(__file__).with_name("config.yaml")))
    args = ap.parse_args()

    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    x = load_npy(cfg["data"]["path"])
    if x.ndim != 2:
        raise ValueError(f"Expected 2D array (n_samples, n_channels), got shape {x.shape}")

    qc_cfg = cfg["qc"]
    out_dir = Path(cfg["output"]["out_dir"])
    fig_dir = out_dir / "figures"
    out_dir.mkdir(parents=True, exist_ok=True)

    rms = rms_per_channel(x)
    frac0 = fraction_zeros_per_channel(x)
    frac_nan = nan_fraction_per_channel(x)


    dead_rms_mask = dead_channels_by_rms(x, min_rms=float(qc_cfg["dead_channel"]["min_rms"]))
    dead_zero_mask = dead_channels_by_zero_fraction(x, max_zero_fraction=float(qc_cfg["dead_channel"]["max_zero_fraction"]))
    dead_any = dead_rms_mask | dead_zero_mask

    rms_outliers = robust_channel_outliers(rms, z_thresh=float(qc_cfg["outliers"]["rms_z_thresh"]))

    segments = find_zero_dropouts(x, min_len=int(qc_cfg["dropouts"]["min_len_samples"]))

    invalid_mask = invalid_channels_by_nan_fraction(
        x,
        max_nan_fraction=float(qc_cfg["invalid"]["max_nan_fraction"]),
    )


    payload = {
        "shape": [int(x.shape[0]), int(x.shape[1])],
        "metrics": {
            "rms_per_channel": rms.astype(float).tolist(),
            "fraction_zeros_per_channel": frac0.astype(float).tolist(),
            "nan_fraction_per_channel": frac_nan.astype(float).tolist(),
        },
        "flags": {
            "invalid_channels": np.flatnonzero(invalid_mask).astype(int).tolist(),
            "dead_channels_by_rms": np.flatnonzero(dead_rms_mask).astype(int).tolist(),
            "dead_channels_by_zero_fraction": np.flatnonzero(dead_zero_mask).astype(int).tolist(),
            "dead_channels": np.flatnonzero(dead_any).astype(int).tolist(),
            "rms_outliers": np.flatnonzero(rms_outliers).astype(int).tolist(),
        },
        "dropout_segments": [asdict(s) for s in segments],
        "config_used": cfg,
    }

    json_path = out_dir / "qc_report.json"
    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    info(f"Wrote JSON report: {json_path}")

    md_path = out_dir / "qc_report.md"
    _write_md_report(md_path, payload)
    info(f"Wrote Markdown report: {md_path}")

    if bool(cfg["output"].get("make_figures", True)):
        save_channel_time_heatmap(x, fig_dir / "heatmap.png", title="Raw data (channel–time)")
        save_rms_bar(rms, fig_dir / "rms_per_channel.png")
        info(f"Wrote figures to: {fig_dir}")

if __name__ == "__main__":
    main()
