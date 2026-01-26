"""
Test all package installations and versions
"""

import sys
print(f"Python version: {sys.version}")
print("=" * 70)

packages = {
    'torch': 'PyTorch',
    'torchvision': 'TorchVision',
    'numpy': 'NumPy',
    'pandas': 'Pandas',
    'sklearn': 'Scikit-learn',
    'matplotlib': 'Matplotlib',
    'seaborn': 'Seaborn',
    'cv2': 'OpenCV',
    'PIL': 'Pillow',
    'plotly': 'Plotly',
    'netcal': 'NetCal',
    'yaml': 'PyYAML',
    'gradio': 'Gradio',
    'scipy': 'SciPy',
    'tqdm': 'tqdm'
}

print("\nPackage Versions:")
print("-" * 70)

all_ok = True
for module, name in packages.items():
    try:
        mod = __import__(module)
        version = getattr(mod, '__version__', 'unknown')
        print(f"✓ {name:20s} {version}")
    except ImportError as e:
        print(f"✗ {name:20s} NOT INSTALLED")
        all_ok = False

print("=" * 70)

# Test PyTorch GPU
if all_ok:
    import torch
    print(f"\nPyTorch Configuration:")
    print(f"  CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"  CUDA version: {torch.version.cuda}")
        print(f"  GPU device: {torch.cuda.get_device_name(0)}")
        print(f"  Number of GPUs: {torch.cuda.device_count()}")
    else:
        print(f"  Using CPU only")
    
    # Test a simple operation
    x = torch.randn(3, 3)
    if torch.cuda.is_available():
        x = x.cuda()
    y = x @ x.T
    print(f"\n✓ PyTorch test operation successful")
    print(f"  Device: {y.device}")

if all_ok:
    print("\n" + "=" * 70)
    print("✓ ALL PACKAGES INSTALLED SUCCESSFULLY!")
    print("=" * 70)
else:
    print("\n" + "=" * 70)
    print("✗ Some packages failed to install. Check errors above.")
    print("=" * 70)