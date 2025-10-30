"""sample_14_04.py - Generator to create Fibonacci numbers"""


def fibonacci_generator(count: int):
    """
    Generator to produce a sequence of 'count' Fibonacci numbers

    Args:
        count: Number of Fibonacci numbers to generate.
    """
    u, v = 0, 1
    yield u
    for _ in range(1, count):
        u, v = v, u + v
        yield u


def main():
    """Demonstration of generator without reference to a known number of elements"""
    for idx, n in enumerate(fibonacci_generator(20)):
        print(f"{idx}: {n}")


if __name__ == "__main__":
    main()
