import sys
import torch
import pandas as pd
import sklearn

def main():
    print(f"Python: {sys.version.split()[0]}")
    print(f"Pandas: {pd.__version__}")
    print(f"Scikit-Learn: {sklearn.__version__}")
    print(f"PyTorch: {torch.__version__}")

    # Korrigerad stavning: is_available
    cuda_available = torch.cuda.is_available()
    print(f"GPU/CUDA Available: {cuda_available}")

    if cuda_available:
        print(f"Device name: {torch.cuda.get_device_name(0)}")

    device = "cuda" if cuda_available else "cpu"
    
    # Skapar tensorer och flyttar till enhet
    try:
        t1 = torch.ones(2, 2).to(device)
        t2 = t1 * 2
        print(f"Tensor Calculation on {device}: Success (Result sum: {t2.sum().item()})")
    except Exception as e:
        print(f"Tensor Calculation on {device}: Failed ({e})")

if __name__ == "__main__":
    main()