"""sample_12_03b.py - Set Initialization using comprehension"""


def init_set(num: int) -> set[int]:
    """
    Generate a set of odd squares < num*num

    Args:
        num: Limit of the elements in the set

    Returns:
        Set of odd squares less than num * num
    """
    return {n * n for n in range(num) if n % 2 == 1}


def main():
    """Main function"""
    result = init_set(10)

    print(result)


if __name__ == "__main__":
    main()
