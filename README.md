# Uncertainty-Aware Skin Cancer Detection with Calibrated Deferral

A medical AI system for melanoma detection that provides calibrated uncertainty estimates and intelligent deferral to dermatologists.

## Project Overview

This project implements a skin lesion classifier with:
- Binary classification (melanoma vs benign)
- Uncertainty quantification (MC Dropout, Deep Ensembles, Evidential DL)
- Calibrated confidence scores
- Deferral mechanism for high-uncertainty cases
- Interactive Gradio demo

**Status:** Phase 0 - Foundation & Setup (In Progress)

## Requirements

- Python 3.12+
- PyTorch 2.3+
- CUDA 12.1+ (for GPU support, recommended)
- 16GB RAM minimum (32GB recommended)
- ~50GB disk space for dataset

## Setup
```bash
# Clone repository
git clone https://github.com/cesaraha/skin-cancer-uncertainty
cd skin-cancer-uncertainty

# Create environment
conda create -n skin-cancer python=3.12 -y
conda activate skin-cancer

# Install PyTorch (with CUDA 12.1)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121

# Install dependencies
pip install -r requirements.txt

# Verify installation
python test_imports.py
```

## Dataset

ISIC 2018 Challenge Dataset
- Training: ~7,000 images
- Validation: ~1,500 images
- Test: ~1,500 images (held out)

Download instructions in `docs/dataset_setup.md`

## Project Structure
```
skin-cancer-uncertainty/
├── data/                    # Dataset (gitignored)
├── src/                     # Source code
│   ├── models/             # Model architectures
│   ├── data/               # Data loaders
│   ├── training/           # Training utilities
│   ├── evaluation/         # Evaluation metrics
│   └── utils/              # Utilities
├── notebooks/              # Jupyter notebooks
├── configs/                # Configuration files
├── experiments/            # Experiment results
├── outputs/                # Plots and visualizations
├── docs/                   # Documentation
└── models/                 # Saved model checkpoints
```

## Phases

- [x] **Phase 0**: Foundation & Setup (26/01-01/02/2026)
- [ ] **Phase 1**: Baseline Classifier (02/02-10/02/2026)
- [ ] **Phase 2**: Monte Carlo Dropout (11/02-19/02/2026)
- [ ] **Phase 3**: Deep Ensembles (20/02-28/02/2026)
- [ ] **Phase 4**: Evidential Deep Learning (optional)
- [ ] **Phase 5**: Deferral & Demo (01/03-07/03/2026)
- [ ] **Phase 6**: Evaluation & Documentation (08/03-14/03/2026)

## Regulatory Context

Designed with EU MDR (Medical Device Regulation 2017/745) compliance in mind:
- Uncertainty quantification for transparency
- Deferral mechanism for safety
- Documentation of limitations
- Performance tracking

## Technology Stack

- **Language**: Python 3.12
- **Deep Learning**: PyTorch 2.3+
- **Data Science**: NumPy, Pandas, Scikit-learn
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Calibration**: NetCal
- **Interface**: Gradio

## Author

César Hernandez Alvarez

## License

MIT License

## Acknowledgments

- ISIC Archive for providing the ISIC 2018 Challenge dataset
- Authors of the research papers cited in `docs/references.md`
- Open-source community for PyTorch, scikit-learn, and related libraries