"""sample_11_06.py - Sample showing how to use runtime assertion"""


def main():
    """Main function handling the exceptions"""
    x = input("Enter an integer value: ")
    try:
        assert x.isdecimal(), f"{x} is not an integer value"
        x = int(x)
        print(f"{type(x)}")
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
