"""circle.py - Defines a circle class"""

import math


class Circle:
    """Defines a circle"""

    # Class variable
    PI = math.pi

    def __init__(self, radius: float):
        """
        Initialize the circle

        Args:
            radius: Radius of the circle
        """
        self.radius = radius

    def area(self) -> float:
        """
        Determine the area of the circle
        """
        return Circle.PI * self.radius**2

    def circumference(self) -> float:
        """
        Determine the circumference of the circle
        """
        return 2 * Circle.PI * self.radius

    @staticmethod
    def set_pi(value: float):
        """
        Set pi to be a new value
        """
        Circle.PI = value
