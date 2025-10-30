"""sample_15_01.py - Simple demonstration of class inheritence."""


class Vehicle:
    """Parent class for the child classes below"""

    def __init__(self, vehicle_type: str):
        self.vehicle_type = vehicle_type

    def print_type(self):
        """Common method subclasses can use"""
        print(self.vehicle_type)


class Automobile(Vehicle):
    """Automobile as a child class of a Vehicle"""

    def __init__(self):
        super().__init__("automobile")

    def drive(self):
        """This is how we travel in an automobile"""
        print("driving")


class Airplane(Vehicle):
    """Airplane is a different child class of a Vehicle"""

    def __init__(self):
        super().__init__("airplane")

    def fly(self):
        """This is how we travel in an airplane"""
        print("flying")


def main():
    "Main function for the program"
    car = Automobile()
    plane = Airplane()

    car.print_type()
    car.drive()
    print()
    plane.print_type()
    plane.fly()


if __name__ == "__main__":
    main()
