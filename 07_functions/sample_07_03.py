"""sample_07_03.py - Passing parameters"""


def double(a):
    """Change a to be twice its current value"""
    a += a


# Pass by value
x = 3
print(f"before: {x=}")
double(x)
print(f"after: {x=}")

# Pass a reference as the value
l = [1, 2, 3]
print(f"before: {l=}")
double(l)
print(f"after: {l=}")
