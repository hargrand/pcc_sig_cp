"""sample_17_06.py - A custom decorator to time function execution and demonstrate use of functools.wraps."""

import time
from functools import wraps
from typing import Any, Callable


def time_it(func: Callable) -> Callable:
    """
    A decorator that prints the execution time of the decorated function.
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """The wrapper function that adds the timing logic."""
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds.")
        return result

    return wrapper


@time_it
def sleeper(delay: float) -> str:
    """A sample function that simulates a delay."""
    print(f"--- Running slow_function with a delay of {delay}s ---")
    time.sleep(delay)
    return "Done!"


def main():
    """Main function to demonstrate the timing decorator."""
    sleeper(0.2)
    sleeper(1.5)

    print("Note preservation of the metadata:")
    print(f"  Name: {sleeper.__name__}")
    print(f"  Docstring: {sleeper.__doc__}")


if __name__ == "__main__":
    main()
