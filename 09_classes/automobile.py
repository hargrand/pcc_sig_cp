"""sample_08_01.py - Basic class definition"""


class Automobile:
    """Defines an automobile"""

    def __init__(self, vin: str, make: str, model: str, year: int, miles: int):
        """
        Initialize the automobile

        Args:
            vin: Vehicle Identification Number
            make: Automobile manufacturer
            model: Model of automobile
            year: Production year of the automobile
            miles: Miles on the odometer of the automobile
        """
        self.vin = vin
        self.make = make
        self.model = model
        self.year = year
        self.miles = miles

    def update_mileage(self, miles: int):
        """
        Update the mileage of the automobile
        """
        self.miles = miles
