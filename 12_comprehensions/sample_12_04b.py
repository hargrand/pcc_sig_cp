"""sample_12_04b.py - Dictionary Initialization using comprehension"""


def init_dict(num: int) -> dict[int, int]:
    """
    Generate a dictionary with positive odd interger keys and their squares as the value for each

    Args:
        num: Limit of the elements in the dictionary

    Returns:
        Dictionary with elements of the form (n, n**2)
    """
    return {n: n**2 for n in range(num) if n % 2 == 1}


def main():
    """Main function"""
    result = init_dict(10)

    print(result)


if __name__ == "__main__":
    main()
