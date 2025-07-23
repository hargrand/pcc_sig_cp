"""sample_06_03.py - List methods iteration"""

fruits = ["apple", "blueberry", "banana", "cherry", "orange"]

print("Elements in the fruits list:")
for fruit in fruits:
    print(fruit)

print()
print("Elements of the fruits list and their index in the list")
for index, fruit in enumerate(fruits):
    print(index, fruit)

print()
print("Elements of fruits list in reversed order and their index in the reversed list")
for index, fruit in enumerate(fruits[::-1]):
    print(index, fruit)
