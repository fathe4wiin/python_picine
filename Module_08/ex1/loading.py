import sys
import os
import importlib.metadata
from typing import List, Optional


def get_version(package_name: str) -> Optional[str]:
    """Retrieve the version of an installed package[cite: 163]."""
    try:
        return importlib.metadata.version(package_name)
    except importlib.metadata.PackageNotFoundError:
        return None


def check_dependencies() -> bool:
    """Check for required packages and print status[cite: 163, 165]."""
    required = ["numpy", "pandas", "matplotlib"]
    optional = ["requests"]
    all_found = True

    print("Checking dependencies:")
    for pkg in required + optional:
        version = get_version(pkg)
        if version:
            status = "OK"
            note = "ready"
        else:
            status = "MISSING" if pkg in required else "WARN"
            note = "not installed"
            if pkg in required:
                all_found = False
        
        print(f"[{status}] {pkg} ({version or 'N/A'}) - {note}")

    if not all_found:
        print("\nError: Missing required dependencies.")
        print("Install with pip: pip install -r requirements.txt")
        print("Install with Poetry: poetry install")
        return False
    return True


def show_environment_info() -> None:
    """Display differences in environment management[cite: 163]."""
    print("\nEnvironment Information:")
    if os.environ.get("POETRY_ACTIVE") == "1":
        print("Status: Running in a Poetry-managed environment.")
    elif os.environ.get("VIRTUAL_ENV"):
        print("Status: Running in a standard virtual environment (pip/venv).")
    else:
        print("Status: WARNING - Running in global environment.")


def run_analysis() -> None:
    """Analyze simulated Matrix data and save visualization[cite: 161, 166]."""
    try:
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt

        print("\nAnalyzing Matrix data...")
        # Simulating 1000 data points [cite: 165, 166]
        data = np.random.randn(1000)
        df = pd.DataFrame(data, columns=["Signal"])
        
        print(f"Processing {len(df)} data points...")
        
        plt.figure(figsize=(10, 6))
        plt.hist(df["Signal"], bins=30, color='green', alpha=0.7)
        plt.title("Matrix Data Signal Distribution")
        plt.savefig("matrix_analysis.png")
        
        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")
    except Exception as e:
        print(f"An error occurred during analysis: {e}")


def main() -> None:
    """Main execution flow."""
    print("LOADING STATUS: Loading programs...")
    if check_dependencies():
        show_environment_info()
        run_analysis()


if __name__ == "__main__":
    print("using diff venvs required before submition!!!")
    # main()