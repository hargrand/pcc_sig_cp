"""sample_09_02.py - Demonstration of "dunder" methods"""

from particle import Particle


def main():
    """Program main function."""
    a = Particle(pos=0.0, vel=10.0)
    b = Particle(pos=10.0, vel=20.0)
    c = a + b

    print(f"{a()=} {b()=} {c()=}")
    print(f"{a(1.0)=} {b(1.0)=} {c(1.0)=}")
    print(f"{a(-1.0)=} {b(-1.0)=} {c(-1.0)=}")
    print(f"{a(100.0)=} {b(100.0)=} {c(100.0)=}")


if __name__ == "__main__":
    main()
