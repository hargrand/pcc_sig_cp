"""sample_07_04.py - Some more advanced topics"""

MAX_VALUE = 100


def sum_to_n(n: int) -> int:
    """Use a loop to compute the sum of numbers from 1 to n"""
    result = 0

    for i in range(n + 1):
        result += i

    return result


def alt_sum_to_n(n: int) -> int:
    """Use a more efficient algorithm to get the correct sum"""
    return n * (n + 1) // 2


print(sum_to_n(MAX_VALUE))
print(alt_sum_to_n(MAX_VALUE))
