def bad_function():
    raise ValueError("ValueError: something bad happened")

def good_function():
    print("I'm good")

try:
    bad_function()
except ValueError as e:
    print(e)
except FileNotFoundError as e:
    print(e)
finally:
    print("ending now")