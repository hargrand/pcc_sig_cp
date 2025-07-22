"""
activity_05_01.py - Count the number of times a letter occurs in a string
the user provides.
"""

val = input("What string would you like me to search? ")
letter = input("What letter should I search for? ")

count = val.lower().count(letter.lower())

print(f"The letter '{letter}' occurs {count} times in '{val}'.")
