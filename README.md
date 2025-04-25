# swb_ecco

## 0. Background
This repository contains 


## 1. Dev Environment Setup
Create an environment.
```shell
conda create -n ecco python=3.11
conda activate ecco
pip install -e .
pip install -r requirements-dev.txt
```

Recompile requirements (only required if new dependencies are added or upgrading existing libraries).
```shell
pip install pip-tools
pip-compile requirements.in --upgrade
pip-compile requirements-dev.in --upgrade
```

## 2. Style and Testing
Testing is done using `pytest`.

Docstrings conform to the [numpy docstring style guide](https://numpydoc.readthedocs.io/en/latest/format.html) 
and `flake8` is used to lint.
