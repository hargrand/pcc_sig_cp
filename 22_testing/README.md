# Session 22 - Testing

This provides instructions for building an environmet to run the test suite for session 22.  To do this, you will need to install miniconda (see session 21 for information about installing miniconda; it can be found at https://docs.conda.io/en/latest/miniconda.html)

## Building the conda environment

```bash
conda create -n sig_22
conda activate sig_22
cd pcc_sig_sp/22_testing
pip install -e .
```

## To run unittest from the command line

### Run without coverage

```bash
cd pcc_sig_sp/22_testing/ut
python -m unittest
```

### Run with coverage

```bash
cd pcc_sig_sp/22_testing/ut
coverage run -m unittest
coverage report --show-missing
```

## To run pytest from the command line

### Run without coverage
```bash
cd pcc_sig_sp/22_testing/pt
pytest
```

### Run with coverage

```bash
cd pcc_sig_sp/22_testing/pt
coverage run -m pytest
coverage report --show-missing
```

## Contents

* [src](src/) - Folder containing the sample source code
* [pt](pt/) - Folder containg sample pytest tests
* [ut](ut/) - Folder containing sample unittest tests
* [pyproject.toml](pyproject.toml) - File containing configuraiton information used to create the conda environment (we will cover pyproject.toml in later sessions)
* [README.md](README.md) - This file
