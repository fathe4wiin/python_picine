#!/usr/bin/env python3

import sys
import os
import site


def in_virtualenv():
    return sys.prefix != sys.base_prefix


def get_venv_name():
    return os.path.basename(sys.prefix)


def get_site_packages():
    paths = site.getsitepackages()
    return paths[0] if paths else "Unknown"

def venv_status() -> None:
    print("Inside the Construct")
    print("$> python construct.py")
    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {get_venv_name()}")
    print(f"Environment Path: {sys.prefix}")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print("Package installation path:")
    print(get_site_packages())
    
def no_venv() -> None:
    print("Outside the Matrix")
    print("$> python construct.py")
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate # On Windows")
    print("Then run this program again.")

def main() -> None:
    if not in_virtualenv():
        no_venv()
    else:
        venv_status()


if __name__ == "__main__":
    main()