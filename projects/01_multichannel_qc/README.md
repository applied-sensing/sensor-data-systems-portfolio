# Project 01 — Multichannel QC baseline

## Goal
A repeatable **QC baseline** for multi-channel sensing time-series data:
- identify dead channels
- detect zero-value dropouts (contiguous runs)
- flag channel-level outliers
- produce plots + machine-readable JSON report

Designed to be **domain-agnostic**: DAS-like matrices, acoustic arrays, vibration arrays, structural sensing, etc.

## Input data model
- `x`: numpy array of shape `(n_samples, n_channels)`

## Outputs
Written to `projects/01_multichannel_qc/output/`:
- `qc_report.json`
- `qc_report.md`
- `figures/heatmap.png`
- `figures/rms_per_channel.png`

## Run
From repo root:

```bash
python -m projects.01_multichannel_qc.pipeline --config projects/01_multichannel_qc/config.yaml
```
