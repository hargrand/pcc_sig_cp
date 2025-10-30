"""sample_09_01a.py - Basic class usage"""

from automobile import Automobile


def main():
    """Program main function."""
    camry = Automobile(
        vin="4T1B11HK6JU635263", make="Toyota", model="Camry", year=2018, miles=125365
    )

    thunderbird = Automobile(
        vin="6Y81Z126801", make="Ford", model="Thunderbird", year=1966, miles=78345
    )

    print(f"{camry.miles=}")
    camry.miles = camry.miles + 1285
    print(f"{camry.miles=}")

    print(thunderbird)


if __name__ == "__main__":
    main()
