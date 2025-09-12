"""sample_13_02b.py - Filter a list using lambda"""


def odd_values(max_val: int) -> list[int]:
    """Create a list of odd values upto and including max"""
    return list(filter(lambda x: x % 2 == 1, range(max_val + 1)))


def main():
    """Main function"""
    print(f"Odd values up to 10: {odd_values(10)}")


if __name__ == "__main__":
    main()
