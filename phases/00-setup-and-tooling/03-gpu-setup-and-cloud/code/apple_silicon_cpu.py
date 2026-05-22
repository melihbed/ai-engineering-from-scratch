import torch

if torch.backends.mps.is_available():
    # Apple Silicon shares system RAM with GPU
    import psutil
    ram = psutil.virtual_memory().total / 1e9
    print(f"Total unified memory: {ram:.1f} GB")
    print(f"Largest fp16 model: ~{ram/2:.0f}B parameters")