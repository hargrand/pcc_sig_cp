"""
test_pytest_sample_22_01.py - Unit tests for sample_22_01.py using pytest.
"""

import pytest
from sample_22_01 import fibonacci, factorial  # type: ignore


def fibonacci_test_cases() -> list[tuple[int, int]]:
    """Return a list of test cases for the fibonacci function."""
    return [(0, 0), (1, 1), (5, 5), (10, 55)]


def factorial_test_cases() -> list[tuple[int, int]]:
    """Return a list of test cases for the factorial function."""
    return [(0, 1), (1, 1), (5, 120), (10, 3628800)]


@pytest.mark.parametrize("n, expected", fibonacci_test_cases())
def test_fibonacci(n, expected):
    """Test the fibonacci function."""
    assert fibonacci(n) == expected


def test_fibonacci_negative():
    """Test the fibonacci function with negative input."""
    with pytest.raises(ValueError):
        fibonacci(-1)


@pytest.mark.parametrize("n, expected", factorial_test_cases())
def test_factorial(n, expected):
    """Test the factorial function."""
    assert factorial(n) == expected


def test_factorial_negative():
    """Test the factorial function with negative input."""
    with pytest.raises(ValueError):
        factorial(-1)


if __name__ == '__main__':
    pytest.main()  # pragma: no cover
