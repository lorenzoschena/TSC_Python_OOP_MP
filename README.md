# Object oriented programming (OOP) and parallel computing in Python
## Tools for Scientific Computing (TSC), Research Master Diploma Course, von Karman Institute for Fluid Dynamics 

This repository contains the material for the TSC course on Object oriented programming (OOP) and parallel computing in Python, given at the von Karman Institute for Fluid Dynamics as part of the Research Master Diploma Course.

## Setup Instructions
We provide two options to set up the environment for this course, either via pip or via conda. Beyond the package requirements, you need to ensure to have a Jupyter Notebook environment set up (e.g., via JupyterLab or Jupyter Notebook extension activated in VSCode/PyCharm).

### Option 1: Using pip
1. Ensure you have Python 3.8 or higher installed.
2. Create and activate a virtual environment:
    ```bash
    # Windows
    python -m venv tsc_oop_env
    tsc_oop_env\Scripts\activate

    # Mac/Linux
    python3 -m venv tsc_oop_env
    source tsc_oop_env/bin/activate
    ```
3. Install the packages:
    ```bash
    pip install -r requirements.txt
    ```

### Option 2: Using Conda
1. Ensure you have Anaconda or Miniconda installed.
2. Create the environment from the file (this handles Python version and packages automatically):
    ```bash
    conda env create -f env.yml
    ```
3. Activate the environment:
    ```bash
    conda activate tsc_oop_env
    ```


