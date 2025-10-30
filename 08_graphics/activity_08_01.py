"""activity_08_01.py - Tutle Graphics Draw a House"""

import turtle


def main():
    """Main function of the program"""
    t = turtle.Turtle()

    t.pensize(2)
    t.pencolor("darkblue")
    t.speed(0)

    t.goto(0, -100)
    t.goto(100, -100)
    t.goto(100, 0)
    t.goto(50, 75)
    t.goto(0, 0)
    t.goto(100, 0)

    turtle.done()


if __name__ == "__main__":
    main()
