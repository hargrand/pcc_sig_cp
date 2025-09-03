"""sample_12_01a.py - Traditional List Initialization"""


def init_dict(num: int) -> dict[int, int]:
    """
    Generate a dictionary with odd integers as the keys and the
    associated square of each key as its value.

    Args:
        num: Limit of the elements in the dict

    Returns:
        Dictionary with elements drawn from (n, n*n)
    """
    odd_squares = {}
    for n in range(num):
        if n % 2 == 1:
            odd_squares[n] = n**2

    return odd_squares


def main():
    """Main function"""
    result = init_dict(10)

    print(result)


if __name__ == "__main__":
    main()
