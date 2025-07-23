"""sample_06_01.py - List access"""

fruits = ["apple", "banana", "cherry"]

print(fruits[0])  # apple
print(fruits[-1])  # cherry

fruits[0] = "grape"
print(fruits[0])  # grape


lol = [[1, 2], [3, 4]]

print(f"{lol=} / {len(lol)=}")
