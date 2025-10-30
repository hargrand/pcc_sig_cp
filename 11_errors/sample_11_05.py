"""sample_11_05.py - Sample showing how to raise and catch exceptions"""


def good_function():
    """Good function - no exception"""
    print("I'm good")


def bad_function():
    """Bad function - raises ValueError"""
    raise ValueError("I'm bad")


def main():
    """Main function handling the exceptions"""
    try:
        good_function()
        bad_function()
    except ValueError as e:
        print(e)
    finally:
        print("I'm done")


if __name__ == "__main__":
    main()
