"""sample_17_04.py - Demonstration of the built-in function decorator for caching values."""

from functools import lru_cache
import time


def fibonacci(n):
    """Compute the nth Fibonacci number without caching."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@lru_cache(maxsize=128)
def cached_fibonacci(n: int) -> int:
    """Compute the nth Fibonacci number using caching."""
    if n < 2:
        return n
    return cached_fibonacci(n - 1) + cached_fibonacci(n - 2)


def main():
    """Demonstrate the difference in performance between the two functions."""
    start_time = time.perf_counter_ns()
    result = fibonacci(35)
    elapsed_time = (time.perf_counter_ns() - start_time) * 1e-9
    print(f"       fibonacci(35) = {result} - elapsed time: {elapsed_time} seconds")

    start_time = time.perf_counter_ns()
    result = cached_fibonacci(35)
    elapsed_time = (time.perf_counter_ns() - start_time) * 1e-9
    print(f"cached_fibonacci(35) = {result} - elapsed time: {elapsed_time} seconds")


if __name__ == "__main__":
    main()
