import torch
import pandas as pd 
import sklearn
import sys 

def main():
    print(f"Python: {sys.version.split()[0]}")
    print(f"Pandas: {pd.__version__}")
    print(f"Scikit-Learn: {sklearn.__version__}")
    print(f"Pytorch: {torch.__version__}")

    cuda_avalible = torch.cuda.is_available()
    print(f"GPU/CUBA Avilable: {cuda_avalible}")
    if cuda_avalible:
        print(f"Device name: {torch.cuda.get_device_name(0)}")

    device = "cuda" if cuda_avalible  else "cpu"
    t1 = torch.ones(2, 2).to(device)
    t2 = t1 * 2
    print(f"Tensor Calculation on {device}: Success (Result sum: {t2.sum().item()})")

if __name__ == "__main__":
    main()
