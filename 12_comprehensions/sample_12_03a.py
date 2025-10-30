"""sample_12_01a.py - Traditional List Initialization"""


def init_set(num: int) -> set[int]:
    """
    Generate a set of odd squares

    Args:
        num: Limit of the elements in the set

    Returns:
        Set containing odd square integers
    """
    odd_squares = set()
    for n in range(num):
        if n % 2 == 1:
            odd_squares.add(n**2)

    return odd_squares


def main():
    """Main function"""
    result = init_set(10)

    print(result)


if __name__ == "__main__":
    main()
