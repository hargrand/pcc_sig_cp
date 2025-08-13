"""sample_09_03.py - Demonstration of class attributes and methods"""

import circle


def main():
    """Program main function."""
    c0 = circle.Circle(radius=1.0)
    c1 = circle.Circle(radius=2.0)

    print(f"{circle.Circle.PI=}")
    print(f"{c0.circumference()=} / {c0.area()=}")
    print(f"{c1.circumference()=} / {c1.area()=}")
    print()

    circle.Circle.set_pi(value=22 / 7)

    print(f"{circle.Circle.PI=}")
    print(f"{c0.circumference()=} / {c0.area()=}")
    print(f"{c1.circumference()=} / {c1.area()=}")
    print()


if __name__ == "__main__":
    main()
