"""activity_13_02.py - Use map and reduce to approximate the value of summing negative powers of 2"""

import functools as ft

N = 32


def traditional(max_n: int) -> float:
    """Compute the value using traditional for loop"""
    value = 0
    for n in range(1, max_n + 1):
        value += 2**-n

    return value


def functional(max_n: int) -> float:
    """Compute the value using map and reduce"""
    return ft.reduce(lambda x, y: x + y, map(lambda n: 2**-n, range(1, max_n + 1)))


def main():
    """Main function"""
    print(f"Number of iterations: {N}")
    print(f"Computed value (traditional): {traditional(N)}")
    print(f"Computed value (functional): {functional(N)}")


if __name__ == "__main__":
    main()
