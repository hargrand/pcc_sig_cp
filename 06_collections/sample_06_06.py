"""sample_06_06.py - Set operations"""

fruits = {"apple", "cherry", "banana"}
trees = {"birch", "apple", "maple"}

print("union:", fruits.union(trees))
print("union:", fruits | trees)

print()
print("intersection:", fruits.intersection(trees))
print("intersection:", fruits & trees)

print()
print("difference 1:", fruits.difference(trees))
print("difference 1:", fruits - trees)

print()
print("difference 2:", trees.difference(fruits))
print("difference 2:", trees - fruits)

print()
print("symmetric_difference:", trees.symmetric_difference(fruits))
print("symmetric_difference:", trees ^ fruits)
