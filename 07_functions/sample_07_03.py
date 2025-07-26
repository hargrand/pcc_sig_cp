"""sample_07_03.py - Using type hint and default values"""


def typed_greeting(name: str) -> str:
    """
    Build a greeting which can be used elsewhere with paramter and return types
    specified
    """
    return f"1. Hello, {name}!"


def default_greeting(name: str = "World") -> str:
    """
    Build a greeting which can be used elsewhere with paramter and return types
    specified and a default value of the name argument is provided for
    situations where no value is given when the function is called.
    """
    return f"2. Hello, {name}!"


print(typed_greeting("World"))
print(default_greeting("Gus"))
print(default_greeting())
# print(default_greeting(4))
