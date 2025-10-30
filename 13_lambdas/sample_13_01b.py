"""sample_13_01a.py - Add 10 using a lambda"""

from typing import Callable


def gen_string(value: float, fn: Callable[[float], float]) -> str:
    """Generate a string given a value and function"""
    return f"{value} + {fn(0.0)} = {fn(value)}"


def main():
    """Main function"""
    values = [5.0, 16.0, 27.0, 38.0, 49.0]
    strings = [gen_string(x, lambda x: x + 10.0) for x in values]
    for string in strings:
        print(string)


if __name__ == "__main__":
    main()
