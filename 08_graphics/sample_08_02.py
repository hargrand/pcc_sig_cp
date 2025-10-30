"""sample_08_02.py - Tutle Graphics Draw 20 perpendicular width 2 lines of length 100"""

import turtle
import math

t = turtle.Turtle()
# t.pensize(5)

t.radians()
t.left(math.pi / 2.0)
t.forward(100)

t.degrees()
t.left(90)
t.forward(100)

turtle.done()
