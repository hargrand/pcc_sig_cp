"""sample_13_03a.py - Reduce a list using function"""

from functools import reduce


def add(x: int, y: int) -> int:
    """Return the sum of x and y"""
    return x + y


def sum1(max_val: int) -> int:
    """Create a the squares of 0..max_val-1"""
    return reduce(add, range(max_val))


def sum2(max_val: int) -> int:
    """Use a shorcut to compute the sum."""
    return max_val * (max_val - 1) // 2


def main():
    """Main function"""
    print(f"sum of elements in range(10): {sum1(10)}")
    print(f"sum of elements in range(10): {sum2(10)}")


if __name__ == "__main__":
    main()
