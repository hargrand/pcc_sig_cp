"""sample_08_06.py - Tutle Graphics Draw a Regular Polygon"""

import turtle


def draw_polygon(t: turtle.Turtle, sides: int, side_length: int):
    """Draw a polygon starting in the turtle's current position"""
    t.setheading(0.0)
    t.forward(side_length)
    for _ in range(sides - 1):
        t.left(360.0 / sides)
        t.forward(side_length)


def teleport(t: turtle.Turtle, x: float, y: float):
    """Move turtle to new position without drawing"""
    t.up()
    t.goto(x, y)
    t.down()


def main():
    """Main function of the program"""
    t = turtle.Turtle()

    t.pensize(5)
    t.pencolor("darkblue")
    t.fillcolor("lightgreen")

    for i in range(3, 7):
        pos = (i - 5) * 150
        teleport(t, pos, pos)
        t.begin_fill()
        draw_polygon(t, i, 100)
        t.end_fill()

    turtle.done()


if __name__ == "__main__":
    main()
