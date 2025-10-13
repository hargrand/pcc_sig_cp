"""sample_17_07.py - A class decorator for logging method calls."""

import logging
from functools import wraps
from typing import Callable, Type

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def log_method(func: Callable):
    """Function decorator function to log method calls."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        # args[0] is 'self'. We log the actual arguments passed to the method.
        info = f"Entering: {func.__qualname__} with args={args[1:]}, kwargs={kwargs}"
        logging.info(info)
        result = func(*args, **kwargs)
        info = f"Exiting: {func.__qualname__} (returned {result!r})"
        logging.info(info)
        return result

    return wrapper


def log_all_methods(cls: Type) -> Type:
    """Class decorator function to log all methods of a class."""
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value) and not attr_name.startswith("__"):
            setattr(cls, attr_name, log_method(attr_value))
    return cls


@log_all_methods
class Calculator:
    """A simple calculator class to demonstrate the logging decorator."""

    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtract two numbers."""
        return a - b

    def hello(self, name: str):
        """Say hello to a person."""
        print(f"Hello, {name}!")


def main():
    """Main function to demonstrate the logging decorator."""
    calc = Calculator()
    calc.add(10, 5)
    calc.subtract(a=20, b=7)
    calc.hello("Alice")

    # Note the method metadata is preserved
    print(f"  Name: {calc.add.__name__}")
    print(f"  Docstring: {calc.add.__doc__}")


if __name__ == "__main__":
    main()
