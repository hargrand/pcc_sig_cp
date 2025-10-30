"""
activity_16_01.py - Adapting the Shape activity from session 15 to use an
Abstract Base Class.
"""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Create an abstract base classfor shapes
    """

    @abstractmethod
    def area(self) -> float:
        """
        Return 0 since we don't know the shape to compute the area
        """

    @abstractmethod
    def perimeter(self) -> float:
        """
        Return 0 since we don't know the shape to compute the perimeter
        """


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


def show_metrics(shape: Shape):
    """Show the shape metrics"""
    try:
        print(f"type = {type(shape)}; {vars(shape)}")
        print(f"area = {shape.area()}")
        print(f"perimeter = {shape.perimeter()}")
    except AttributeError as err:
        print(f"{type(shape)}: {str(err)}")


CIRCLE_RADIUS = 10.0
RECTANGLE_HEIGHT = 20
RECTANGLE_WIDTH = 50


def main():
    """
    Main function
    """
    circle = Circle(radius=CIRCLE_RADIUS)
    show_metrics(circle)

    rectangle = Rectangle(height=RECTANGLE_HEIGHT, width=RECTANGLE_WIDTH)
    show_metrics(rectangle)

    # Running with the following lines uncommented will result in an exception
    # being raised

    # other = Shape()
    # show_metrics(other)


if __name__ == "__main__":
    main()
