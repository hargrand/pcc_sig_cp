"""sample_07_06.py - Input validation"""


def fahrenheit_to_celsius(f):
    """Convert a temperature in degrees F to degrees C"""
    if not isinstance(f, (float, int)):
        return None

    return (f - 32) * 5 / 9


print(fahrenheit_to_celsius(32))
print(fahrenheit_to_celsius(212.0))
print(fahrenheit_to_celsius(-40.0))
print(fahrenheit_to_celsius("Hello, World!"))
