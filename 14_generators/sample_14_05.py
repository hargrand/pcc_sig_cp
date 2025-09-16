"""sample_14_03.py - Use of generator expressions"""

N = 11


def cubes(max_n: int):
    """Define a generator for cube values"""
    for n in range(max_n):
        yield n**3


def main():
    """Demonstration of generator expression"""
    ge = (n**3 for n in range(N))

    print("Use of generator expression:")
    for n in ge:
        print(n)

    print("Use of function which acts as a generator:")
    for n in cubes(N):
        print(n)


if __name__ == "__main__":
    main()
