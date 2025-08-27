"""sample_11_01.py - Basic sample using build in exception generation"""


def main():
    """Main function for this sample"""
    x = input("Enter a number: ")
    try:
        x = int(x)
        print(10 / x)
    except ZeroDivisionError:
        print("You cannot divide by zero!")
    except ValueError:
        print(f"'{x}' is not a valid number")


if __name__ == "__main__":
    main()
