"""sample_07_04.py - Some more advanced topics"""

MAX_VALUE = 100


def bad(n: int) -> int:
    """A bad example of a recursive function"""
    return n + bad(n - 1)


def good(n: int) -> int:
    """A better example of a recursive function"""
    if n <= 0:
        return 0

    return n + good(n - 1)


def alternative(n: int) -> int:
    """Use a loop to compute the sum of numbers from 1 to n"""
    result = 0

    for i in range(n + 1):
        result += i

    return result


def better_alternative(n: int) -> int:
    """Use a more efficient algorithm to get the correct sum"""
    return n * (n + 1) // 2


# print(bad(5))
print(good(MAX_VALUE))
print(alternative(MAX_VALUE))
print(better_alternative(MAX_VALUE))
