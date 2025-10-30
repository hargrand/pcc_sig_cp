"""sample_11_04.py - Exception handler with 'finally' keyword"""


def main():
    """Main function for this sample"""
    x = input("Enter a number: ")
    try:
        x = int(x)
        print(10 / x)
    except ValueError:
        print(f"'{x}' is not a valid number")
    finally:
        print("The end")


if __name__ == "__main__":
    main()
