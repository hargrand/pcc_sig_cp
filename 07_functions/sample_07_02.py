"""sample_07_01.py - Passing parameters"""


def add(a, b):
    """Apply the + operator to two operands and return the result"""
    return a + b


print(add(3, 5))
print(add(5.2, 4.9))
print(add("Hello, ", "World!"))
print(add(True, False))
print(add([1, 2, 3], [4, 5, 6]))


def generate_greeting(name):
    """Build a greeting which can be used elsewhere"""
    return f"3. Hello, {name}!"


def typed_generate_greeting(name: str) -> str:
    """
    Build a greeting which can be used elsewhere with paramter and return types
    specified
    """
    return f"4. Hello, {name}!"


def default_generate_greeting(name: str = "World") -> str:
    """
    Build a greeting which can be used elsewhere with paramter and return types
    specified and a default value of the name argument is provided for
    situations where no value is given when the function is called.
    """
    return f"5. Hello, {name}!"


print(generate_greeting("World"))
print(generate_greeting(4))
print(typed_generate_greeting("World"))
print(default_generate_greeting("Gus"))
print(default_generate_greeting())
# print(default_generate_greeting(4))
