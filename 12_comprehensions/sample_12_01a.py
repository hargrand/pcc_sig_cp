"""sample_12_01a.py - Traditional List Initialization"""


def init_list(num: int) -> list[int]:
    """
    Generate a list of odd squares < num*num

    Args:
        num: Limit of the elements in the list

    Returns:
        List of odd squares less than num * num
    """
    odd_squares = []
    for n in range(num):
        if n % 2 == 1:
            odd_squares.append(n * n)

    return odd_squares


def main():
    """Main function"""
    result = init_list(10)

    print(result)


if __name__ == "__main__":
    main()
