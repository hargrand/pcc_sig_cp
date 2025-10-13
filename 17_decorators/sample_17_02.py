"""sample_17_02.py - Decorator usage - property setter / getter"""

import math


class Circle:
    """Sample class showing the use of pre-defined decorators"""

    def __init__(self, radius: float):
        self.radius = radius

    @property
    def area(self) -> float:
        """Retrieve the area of the circle"""
        return self.radius**2 * math.pi

    @area.setter
    def area(self, area: float):
        """Set the area of the circle"""
        self.radius = math.sqrt(area / math.pi)


def main():
    """Main function for the sample"""
    circle = Circle(radius=10)
    print(f"{circle.radius=:.4f}\t{circle.area=:.4f}")
    circle.area = 600
    print(f"{circle.radius=:.4f}\t{circle.area=:.4f}")


if __name__ == "__main__":
    main()
