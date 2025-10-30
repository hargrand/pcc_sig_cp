"""particle.py - Defines a class for a particle in constant velocity"""


class Particle:
    """Defines a particle position in constant velocity from a starting position"""

    def __init__(self, pos: float, vel: float):
        """
        Initialize the particle

        Args:
            pos: particle starting position (at time = 0)
            vel: particle constant velocity
        """
        self.pos = pos
        self.vel = vel

    def __call__(self, time: float = 0.0) -> float:
        """
        Determine the particle position at the given time

        Args:
            time: Time we'd like to know the position of the particle
        """
        return self.pos + time * self.vel

    def __add__(self, other: "Particle") -> "Particle":
        """create a new particle that is the average of the two given"""
        return Particle((self.pos + other.pos) / 2.0, (self.vel + other.vel) / 2.0)
