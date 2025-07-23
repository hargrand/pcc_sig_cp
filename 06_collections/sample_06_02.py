"""sample_06_02.py - List methods and functions"""

fruits = ["apple", "banana", "cherry"]

fruits.append("orange")  # add orange to the end of the list
print(f'after fruits.append("orange"): {fruits=} - {len(fruits)=}')

fruits.insert(1, "blueberry")  # Insert blueberry after apple
print(f'after fruits.insert(1, "blueberry"): {fruits=} - {len(fruits)=}')

fruits.remove("banana")  # Remove banana from the list
print(f'after fruits.remove("banana"): {fruits=} - {len(fruits)=}')

last = fruits.pop()  # Remove the last element from the list
print(f"after fruits.pop(): {fruits=} - {len(fruits)=}")
print(f"after fruits.pop(): {last=}")
