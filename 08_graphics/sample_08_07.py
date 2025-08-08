"""sample_08_07.py - Tutle Graphics Simple Rule; Complex Image"""

import turtle


def main():
    """Main function of the program"""
    t = turtle.Turtle()

    turtle.Screen().bgcolor("black")
    t.speed(speed=0)
    t.pensize(2)

    t.up()
    t.forward(100)
    t.down()

    for _ in range(72):
        t.left(80)
        t.pencolor("red")
        t.forward(200)
        t.left(150)
        t.pencolor("green")
        t.forward(200)
        t.left(45)
        t.pencolor("blue")
        t.forward(200)

    turtle.done()


if __name__ == "__main__":
    main()
