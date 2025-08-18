"""vector.py - Vector class"""

import math


class Vector:
    """Vector class"""

    def __init__(self, x: float, y: float):
        """Constructor"""
        self.x = x
        self.y = y

    def length(self) -> float:
        """Return the length of the vector"""
        return math.sqrt(self.x**2 + self.y**2)

    def direction(self) -> float:
        """Return the direction of the vector"""
        return math.atan2(self.y, self.x)

    def __add__(self, other: "Vector") -> "Vector":
        """Add one vector to another vector"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        """Subtract one vector from another vector"""
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self) -> str:
        """Return a string representation of the vector"""
        return f"({self.x}, {self.y})"
