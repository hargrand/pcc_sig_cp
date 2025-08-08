"""activity_08_01.py - Draw a spirogram"""

import turtle
import math


def teleport(t: turtle.Turtle, x: float, y: float):
    """Move turtle to new position without drawing"""
    t.up()
    t.goto(x, y)
    t.down()


def main():
    """Main function of the program"""
    t = turtle.Turtle()

    steps = 60
    major_radius = 100
    minor_radius = 75
    t.pensize(2)
    t.pencolor("darkblue")
    t.radians()
    t.speed(0)

    for i in range(steps):
        angle = 2 * math.pi * i / steps
        x = major_radius * math.cos(angle)
        y = major_radius * math.sin(angle)
        teleport(t, x, y)
        t.circle(minor_radius)

    turtle.done()


if __name__ == "__main__":
    main()
