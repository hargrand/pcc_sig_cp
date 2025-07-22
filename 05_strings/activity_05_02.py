"""activity_05_02.py - Prompts the user for a sentance and manipulates the string"""

sentance = input("Please enter a sentance to analyze: ")

print(f"Performing analysis on the sentance: '{sentance}'")
print(f"The sentance in upper case: '{sentance.upper()}'")
print(f"The sentance has {len(sentance.split(' '))} words.")
print(f"The first character of the sentance is '{sentance[0]}'.")
print(f"The last character of the sentance is '{sentance[-1]}'.")

print("The sentance with spaces replaced by underscores, two methods:")
print(f"  method 1: {sentance.replace(' ', '_')}")
print(f"  method 2: {'_'.join(sentance.split(' '))}")
