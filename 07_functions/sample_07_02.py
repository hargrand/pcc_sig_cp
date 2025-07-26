"""sample_07_02.py - Returning values"""


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
    return f"Hello, {name}!"


print(generate_greeting("World"))
print(generate_greeting(4))
