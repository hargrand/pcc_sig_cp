"""activity_15_02.py - Example showing how to use inheritance"""


class Employee:
    """
    Base class for child classes defining the area and perimter of the shape
    """

    def __init__(self, name: str):
        self._name = name

    def name(self) -> str:
        """Retrieve the employee name"""
        return self._name


class Manager(Employee):
    """
    Implements the Shape class but tailored for a circle
    """

    def __init__(self, name: str, department: str):
        """
        Define a manager given a name and department

        Args:
            radius: Radius of the circle instantiated
        """
        super().__init__(name=name)
        self._department = department

    def department(self) -> str:
        """
        Return the department the manager is responsible for managing

        Returns
            Area of the circle
        """
        return self._department


def main():
    """
    Main function
    """
    employee = Employee(name="Richard Smith")
    manager = Manager(name="George Jones", department="Accounting")

    print(f"Employee: name = {employee.name()}")
    print(f"Manager: name = {manager.name()}; dept = {manager.department()}")


if __name__ == "__main__":
    main()
