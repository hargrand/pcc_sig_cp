"""sample_14_03.py - Catching and handling the StopIteration exception"""


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
    """Demonstration of generator without reference to a known number of elements"""
    gen_0 = my_range(0, 10)
    print("Values in range 0..10")
    while True:
        try:
            print(next(gen_0))
        except StopIteration:
            break


if __name__ == "__main__":
    main()
