"""sample_07_05.py - Recursive functions"""

MAX_VALUE = 100


def bad_sum_to_n(n: int) -> int:
    """A bad example of a recursive function"""
    return n + bad_sum_to_n(n - 1)


def recursive_sum_to_n(n: int) -> int:
    """A better example of a recursive function"""
    if n <= 0:
        return 0

    return n + recursive_sum_to_n(n - 1)


# print(bad_sum_to_n(MAX_VALUE))
print(recursive_sum_to_n(MAX_VALUE))
