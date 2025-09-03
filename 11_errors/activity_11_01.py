"""activity_11_01.py - Validate input from the user to convert degrees F to degrees C"""


def get_deg_f() -> float:
    """Prompt user for a numeric value representing degrees F"""
    while True:
        try:
            value = input("Enter a temp (F) to convert to C: ")
            return float(value)
        except ValueError as err:
            print(err)
            print(f"'{value}' is not a valid number. Try again.")


def convert_f_to_c(deg_f: float) -> float:
    """Convert a value from degrees F to degrees C"""
    return (deg_f - 32.0) * 5 / 9


def main():
    """Main function"""
    deg_f = get_deg_f()
    deg_c = convert_f_to_c(deg_f=deg_f)

    print(f"{deg_f} F = {deg_c} C")


if __name__ == "__main__":
    main()
