# Sensor Data Systems Portfolio

Reproducible analysis and validation workflows for **noise-affected multi-channel sensing data**.

This repository is intentionally structured like an engineering deliverable (not a notebook dump):
- **data I/O + metadata handling**
- **quality control (QC)**
- **preprocessing**
- **feature extraction**
- **visualization**
- **pipelines** for batch evaluation and reporting

Applicable across domains such as:
- distributed acoustic sensing (DAS)
- acoustic / ultrasonic arrays
- seismic and vibration monitoring
- structural health sensing
- environmental and infrastructure monitoring

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r environment/requirements.txt
python -m pipelines.batch_validation.run_validation --help
```
    
## Repository map

- `core/` reusable library code (I/O, QC, preprocessing, features, visualization)
- `pipelines/` executable pipelines (batch validation, sensor health, event detection, etc.)
- `projects/` narrative, self-contained mini-studies (each has its own README + configs)
- `datasets/` synthetic + public data pointers (no large files committed)
- `docs/` engineering notes: architecture, validation philosophy, roadmap

## Status

Starter scaffold generated on 2026-01-26. Replace placeholder logic with real implementations as you add projects.

## Example: run Project 01 (multichannel QC)

```bash
python -m projects.01_multichannel_qc.pipeline --config projects/01_multichannel_qc/config.yaml
```
