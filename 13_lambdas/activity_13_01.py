"""activity_13_01.py - Use map and reduce to approximate the value of (pi^2)/6"""

import functools as ft
import math

N = 100
RESULT = (math.pi**2) / 6.0


def traditional(max_n: int) -> float:
    """Compute the sum using a traditional for loop"""
    value: float = 0.0
    for n in range(1, max_n + 1):
        value += n**-2

    return value


def functional(max_n: int) -> float:
    """Compute the sum using map and reduce"""
    return ft.reduce(lambda x, y: x + y, map(lambda n: n**-2, range(1, max_n + 1)))


def main():
    """Main function"""

    print(f"Number of iterations: {N}")
    print(f"Actual value: {RESULT}")
    trad = traditional(N)
    func = functional(N)
    print(f"Computed value (traditional): {trad} / diff: {math.fabs(RESULT - trad)}")
    print(f"Computed value (functional) : {func} / diff: {math.fabs(RESULT - func)}")


if __name__ == "__main__":
    main()
