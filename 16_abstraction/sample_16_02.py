"""sample_16_02.py - Example showing how to use a protocol class"""

from typing import Protocol


class Faithful(Protocol):
    """Protocol for defining a Faithful Christian"""

    def love(self):
        """A faithful person must express love"""

    def faith(self) -> float:
        """A faithful person must express faith"""


class Agnostic:
    """Class defining an agnostic"""

    def love(self):
        """Express love"""
        print("has love of the world")

    def skepticism(self):
        """Express skepticism"""
        print("has skepticism")


class Christian:
    """Class defining a Christian"""

    def love(self):
        """Express love"""
        print("has love of God")

    def faith(self):
        """Express faith"""
        print("has faith")


def express_faith(person: Faithful):
    """Show you have faith..."""
    print(type(person))
    person.love()
    person.faith()


def main():
    """Main function"""

    alice = Christian()
    bob = Agnostic()

    express_faith(person=alice)
    express_faith(person=bob)


if __name__ == "__main__":
    main()
