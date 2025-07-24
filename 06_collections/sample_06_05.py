"""sample_06_05.py - Set manipulation"""

fruits = {"apple", "cherry", "banana"}

# print(fruits[0])

print()
for fruit in fruits:
    print(fruit)

print()
# sos = {{1, 2}, {3, 4}}
# sol = {[1, 2], [3, 4]}
sot = {(1, 2), (3, 4)}

print(f"{sot=} / {len(sot)=}")

print((1,3) in sot)
