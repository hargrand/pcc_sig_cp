"""sample_12_02.py - Tuple Initialization using comprehension"""


def init_tuple(num: int) -> tuple[int, ...]:
    """
    Generate a list of odd squares < num*num

    Args:
        num: Limit of the elements in the list

    Returns:
        List of odd squares less than num * num
    """
    return tuple(n * n for n in range(num) if n % 2 == 1)


def main():
    """Main function"""
    result = init_tuple(10)

    print(result)


if __name__ == "__main__":
    main()
