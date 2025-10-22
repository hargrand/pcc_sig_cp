"""activity_17_01.py - Profile two methods of computing Fibonacci numbers."""

from functools import lru_cache, wraps
import time
from typing import Callable, Type

call_dict: dict[str, list[float]] = {}


def profile_method(func: Callable):
    """Function decorator function to profile method calls."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end_time = time.perf_counter_ns()
        if func.__qualname__ not in call_dict:
            call_dict[func.__qualname__] = []
        call_dict[func.__qualname__].append((end_time - start_time) * 1e-9)
        return result

    return wrapper


def profile_all_methods(cls: Type) -> Type:
    """Class decorator function to profile all methods of a class."""
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value) and not attr_name.startswith("__"):
            setattr(cls, attr_name, profile_method(attr_value))
    return cls


@profile_all_methods
class Fibonacci:
    """A simple calculator class to demonstrate the logging decorator."""

    @staticmethod
    def standard(n):
        """Compute the nth Fibonacci number without caching."""
        if n < 2:
            return n
        return Fibonacci.standard(n - 1) + Fibonacci.standard(n - 2)

    @staticmethod
    @lru_cache(maxsize=128)
    def cached(n: int) -> int:
        """Compute the nth Fibonacci number using caching."""
        if n < 2:
            return n
        return Fibonacci.cached(n - 1) + Fibonacci.cached(n - 2)


def summary():
    """Display a summary of the profile results"""
    for func_name, calls in call_dict.items():
        total_time = sum(calls)
        max_time = max(calls)
        call_count = len(calls)
        avg_time = total_time / call_count
        print(f"Function {func_name}:")
        print(f"  Total time: {total_time} seconds")
        print(f"  Max time per call: {max_time} seconds")
        print(f"  Call count: {call_count}")
        print(f"  Average time per call: {avg_time} seconds")
        print()


def main():
    """Main function to demonstrate the logging decorator."""
    result = Fibonacci.standard(35)
    print(f"       fibonacci(35) = {result}")
    result = Fibonacci.cached(35)
    print(f"cached_fibonacci(35) = {result}")
    summary()


if __name__ == "__main__":
    main()
