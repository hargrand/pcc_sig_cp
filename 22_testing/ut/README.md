# Unit tests - unittest

This folder contains the module containing unittes tests for session 22.

## Usage

You will need to create and activate the conda environment containing the code to test and the tools used to run the tests.

### No coverage
```bash
cd pcc_sig_sp/22_testing/ut
python -m unittest
```

### With coverage
```bash
cd pcc_sig_sp/22_testing/ut
coverage run -m unittest
coverage report --show-missing
```

## Contents

* [test_unittest_session_22_01.py](test_unittest_session_22_01.py) - unittest test for the session_22_01.py module
* [\_\_init\_\_.py](__init__.py) - This file is used to mark this folder as a python package which can be imported, or in this case, marked as containing tests to run.  If missing, the unittest tool may not find the tests.
* [README.md](README.md) - This file
