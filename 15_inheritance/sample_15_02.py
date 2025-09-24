"""sample_15_02.py - Overriding a method."""


class Vehicle:
    """Parent class for the child classes below"""

    def __init__(self, vehicle_type: str):
        self.vehicle_type = vehicle_type

    def print_type(self):
        """Common method subclasses can use"""
        print(self.vehicle_type)

    def move(self):
        """Base class "move"."""
        self.print_type()


class Automobile(Vehicle):
    """Automobile as a child class of a Vehicle"""

    def __init__(self):
        super().__init__("automobile")

    def move(self):
        """This is how we travel in an automobile"""
        super().move()
        print("driving")


def main():
    "Main function for the program"
    car = Automobile()
    car.move()

    generic = Vehicle("generic")
    generic.move()


if __name__ == "__main__":
    main()
