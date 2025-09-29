"""activity_15_01.py - Example showing how to use inheritance"""

import math


class Shape:
    """
    Base class for child classes defining the area and perimter of the shape

    We provide basic implementations of area and perimeter, but since we don't
    know what kind of shape we actually are, we can't really give valid values,
    so just return 0.

    We could raise an exception instead to show the methods weren't implemented
    in the sub class, but we won't.
    """

    def area(self) -> float:
        """
        Return 0 since we don't know the shape to compute the area
        """
        return 0.0

    def perimeter(self) -> float:
        """
        Return 0 since we don't know the shape to compute the perimeter
        """
        return 0.0


class Circle(Shape):
    """
    Implements the Shape class but tailored for a circle
    """

    def __init__(self, radius: float):
        """
        Define a circle baed on its radius

        Args:
            radius: Radius of the circle instantiated
        """
        super().__init__()
        self._radius = radius

    def area(self) -> float:
        """
        Compute and return the area of the circle.

        Returns
            Area of the circle
        """
        return math.pi * self._radius**2.0

    def perimeter(self) -> float:
        """
        Compute and return the perimeter of the circle

        Returns
            Perimeter of the circle
        """
        return 2.0 * math.pi * self._radius


class Rectangle(Shape):
    """
    Implements the Shape class but tailored for a rectangle
    """

    def __init__(self, height: float, width: float):
        """
        Define a rectangle based on it height and width

        Args:
            height: Height of the rectangle
            width: Width of the rectangle
        """
        super().__init__()
        self._height = height
        self._width = width

    def area(self) -> float:
        """
        Compute and return the area of the rectangle.

        Returns
            Area of the rectangle
        """
        return self._height * self._width

    def perimeter(self) -> float:
        """
        Compute and return the perimeter of the rectangle

        Returns
            Perimeter of the rectangle
        """
        return 2.0 * (self._height + self._width)


CIRCLE_RADIUS = 10.0

RECTANGLE_HEIGHT = 20
RECTANGLE_WIDTH = 50


def main():
    """
    Main function
    """
    circle = Circle(radius=CIRCLE_RADIUS)

    print(
        f"Circle of radius {CIRCLE_RADIUS} "
        f"has area {circle.area()} and perimter {circle.perimeter()}"
    )

    rectangle = Rectangle(height=RECTANGLE_HEIGHT, width=RECTANGLE_WIDTH)
    print(
        f"Rectangle with height {RECTANGLE_HEIGHT} and width {RECTANGLE_WIDTH} "
        f"has area {rectangle.area()} and perimter {rectangle.perimeter()}"
    )

    other = Shape()
    print(f"Shape has area {other.area()} and perimter {other.perimeter()}")


if __name__ == "__main__":
    main()
