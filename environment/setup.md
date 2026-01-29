# Setup

## venv (recommended)
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r environment/requirements.txt
```

## conda (optional)
```bash
conda env create -f environment/environment.yml
conda activate sensor-portfolio
```

## Notes
- Keep datasets small or synthetic in this repo.
- Prefer deterministic pipelines: configs + fixed random seeds.
