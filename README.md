## ML Environment Setup with uv

This project demonstrates how to set up an isolated, reproducible machine learning development environment using uv for dependency management.

## What the code does

The verification script (check_env.py) validates that your Python environment is correctly configured for machine learning work. It performs the following checks:

Python version: Displays the current Python version

Package versions: Shows installed versions of Pandas, Scikit-Learn, and PyTorch

Hardware acceleration: Detects if GPU/CUDA is available on your system

Device selection: Automatically selects "cuda" if available, otherwise falls back to "cpu"

Tensor computation: Creates a simple tensor and performs a multiplication to verify that computations work correctly on the selected device

Error handling: Gracefully handles any failures in tensor operations

## Installation Requirements

Based on the code, you need to install the following packages:

text
torch
pandas
scikit-learn
jupyter
Setup Instructions

## Initialize the project with uv:

uv init

## Add the required dependencies:

uv add torch pandas scikit-learn jupyter
Note: PyTorch will automatically be installed with the appropriate version for your hardware when using uv.

## Run the verification script:

uv run check_env.py
The script will output information about your environment and confirm whether tensor calculations work properly on your available hardware (CPU or GPU).

Project Files
pyproject.toml - Project metadata and dependency specifications

uv.lock - Locked dependency versions for reproducibility

check_env.py - Environment verification script

README.md - This documentation file
