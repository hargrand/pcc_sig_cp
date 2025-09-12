"""sample_13_02a.py - Filter a list using function"""


def is_odd(x: int) -> bool:
    """Return true if x is odd; false otherwise"""
    return x % 2 == 1


def odd_values(max_val: int) -> list[int]:
    """Create a list of odd values upto and including max"""
    return list(filter(is_odd, range(max_val + 1)))


def main():
    """Main function"""
    print(f"Odd values up to 10: {odd_values(10)}")


if __name__ == "__main__":
    main()
