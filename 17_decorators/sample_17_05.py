"""sample_17_05.py - A custom decorator demonstrating the basic approach to wrting a decorator"""


def my_decorator(func):
    """A basic custom function decorator"""

    def wrapper():
        """Wrapper to add functionality to the decorated function"""
        print("Before")
        func()
        print("After")

    return wrapper


@my_decorator
def say_hello():
    """A simple function to demonstrate the decorator"""
    print("Hello")


def main():
    """Main function to demonstrate the decorator"""
    say_hello()
    print("\nNote the loss of the function's metadata:")
    print(f"  Name: {say_hello.__name__}")
    print(f"  Docstring: {say_hello.__doc__}")


if __name__ == "__main__":
    main()
