"""sample_13_01a.py - Add 10 using a function"""

from typing import Callable


def add_ten(x: float) -> float:
    """Function which adds 10"""
    return x + 10.0


def gen_string(value: float, adder: Callable[[float], float]) -> str:
    """Generate a string given a value and function"""
    return f"{value} + {adder(0.0)} = {adder(value)}"


def main():
    """Main function"""
    values = [5.0, 16.0, 27.0, 38.0, 49.0]
    strings = [gen_string(value=x, adder=add_ten) for x in values]

    for string in strings:
        print(string)


if __name__ == "__main__":
    main()
