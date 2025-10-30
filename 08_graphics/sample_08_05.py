"""sample_08_06.py - Tutle Graphics Draw a Circle"""

import turtle

t = turtle.Turtle()
t.pensize(3)
for i in range(0, 100, 10):
    t.circle(i)

turtle.done()
