"""
test_unittest_sample_22_01.py - Unit tests for sample_22_01.py using unittest.
"""
import unittest
from sample_22_01 import fibonacci, factorial  # type: ignore


def fibonacci_test_cases() -> list[tuple[int, int]]:
    """Return a list of test cases for the fib function."""
    return [(0, 0), (1, 1), (5, 5), (10, 55)]


def factorial_test_cases() -> list[tuple[int, int]]:
    """Return a list of test cases for the factorial function."""
    return [(0, 1), (1, 1), (5, 120), (10, 3628800)]


class TestSampleFunctions(unittest.TestCase):
    """Unit tests for sample_22_01.py"""

    def run_test_cases(self, func, test_cases):
        """Run the test cases for a given function."""
        for n, expected in test_cases:
            with self.subTest(n=n, expected=expected):
                self.assertEqual(func(n), expected)

    def run_bad_value(self, func, value):
        """Run the test cases for a given function."""
        with self.assertRaises(ValueError):
            func(value)

    def test_fib(self):
        """Test the fib function."""
        self.run_test_cases(fibonacci, fibonacci_test_cases())

    def test_fibonacci_negative(self):
        """Test the fib function with negative input."""
        self.run_bad_value(fibonacci, -1)

    def test_factorial(self):
        """Test the factorial function."""
        self.run_test_cases(factorial, factorial_test_cases())

    def test_factorial_negative(self):
        """Test the factorial function with negative input."""
        self.run_bad_value(factorial, -1)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
