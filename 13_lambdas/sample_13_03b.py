"""sample_13_03a.py - Map a list using function"""


def square_values(max_val: int) -> list[int]:
    """Create a the squares of 0..max_val-1"""
    return list(map(lambda x: x**2, range(max_val)))


def main():
    """Main function"""
    print(f"Squares in range(10): {square_values(10)}")


if __name__ == "__main__":
    main()
