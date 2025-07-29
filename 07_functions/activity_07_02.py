"""activity_07_02.py - Compute the factorial of a number"""

MAX_VALUE = 10


def factorial(n: int) -> int:
    """Compute n! ... n factorial = n*(n-1)*(n-1)* ... *1"""
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def factorial_recursive(n: int) -> int:
    """Compute n! using recursion"""
    if n <= 1:
        return 1

    return n * factorial_recursive(n - 1)


print(factorial(MAX_VALUE))
print(factorial_recursive(MAX_VALUE))
