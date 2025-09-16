"""sample_14_02.py - Use of the next function"""


def my_range(start: int, stop: int, step: int = 1):
    """
    Partial implementation of the standard python range function using a generator

    Args:
        start: Starting point for the range
        stop: Stopping point for the range
        step: Size of each step to take to towards the stopping point

    Yields:
        Next value in the range
    """
    assert step > 0
    value = start
    while value < stop:
        yield value
        value += step


def main():
    """Main function to test the generator function defined above"""
    gen_0 = my_range(0, 10)
    print("Values in range 0..10")
    for _ in range(10):
        print(next(gen_0))


if __name__ == "__main__":
    main()
