"""sample_09_01b.py - Basic class usage"""

from automobile import Automobile


def main():
    """Program main function."""
    camry = Automobile(
        vin="4T1B11HK6JU635263", make="Toyota", model="Camry", year=2018, miles=125365
    )

    print(f"{camry.miles=}")
    camry.update_mileage(miles=camry.miles + 1285)
    print(f"{camry.miles=}")


if __name__ == "__main__":
    main()
