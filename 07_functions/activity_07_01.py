"""activity_07_01.py - Convert Celsius to Fahrenheit"""


def celsius_to_fahrenheit(c):
    """Convert a temperature in degrees C to degrees F"""
    if not isinstance(c, (float, int)):
        return None

    return 32 + 9 * c / 5


print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100.0))
print(celsius_to_fahrenheit(-40.0))
print(celsius_to_fahrenheit("Hello, World!"))
