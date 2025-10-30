"""sample_14_01.py - Implementation of the standard range function... mostly"""


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
    print("Values in range 0..10")
    for value in my_range(0, 10):
        print(value)

    print("Even values in range 0..10")
    for value in my_range(0, 10, 2):
        print(value)


if __name__ == "__main__":
    main()
