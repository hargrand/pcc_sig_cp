# Unit tests - pytest

This folder contains the module containing pytest tests for session 22.

## Usage

You will need to create and activate the conda environment containing the code to test and the tools used to run the tests.

### No coverage
```bash
cd pcc_sig_sp/22_testing/pt
pytest
```

### With coverage
```bash
cd pcc_sig_sp/22_testing/pt
coverage run -m pytest
coverage report --show-missing
```

## Contents

* [test_pytest_session_22_01.py](test_pytest_session_22_01.py) - pytest test for the session_22_01.py module
* [\_\_init\_\_.py](__init__.py) - This file is used to mark this folder as a python package which can be imported, or in this case, marked as containing tests to run.  If missing, the pytest tool may not find the tests.
* [README.md](README.md) - This file
