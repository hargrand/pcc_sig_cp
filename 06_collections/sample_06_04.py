"""sample_06_04.py - Tuple operations"""

fruits = ("apple", "banana", "cherry")

print(fruits[0])  # apple
print(fruits[-1])  # cherry

print()
for fruit in fruits:
    print(fruit)

print()
x, y, z = fruits
print(f"{x=} {y=} {z=}")

print()
tot = ((1, 2), (3, 4))
print(f"{tot=} / {len(tot)=}")

# tot[0] = "food"
