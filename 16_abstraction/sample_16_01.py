"""sample_16_01.py - Example showing how to use an abstract base class"""

from abc import ABC, abstractmethod


class Faithful(ABC):
    """Framework for defining a Faithful person"""

    @abstractmethod
    def love(self):
        """A faithful person must express love"""

    @abstractmethod
    def faith(self) -> float:
        """A faithful person must express faith"""


class Agnostic(Faithful):
    """Class defining an agnostic"""

    def love(self):
        """Express love"""
        print("has love of the world")

    def skepticism(self):
        """Express skepticism"""
        print("has skepticism")


class Christian(Faithful):
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
    express_faith(person=alice)

    # Cannot instantiate an Agnostic since it is defined without a
    # faith method.  If uncommented when run, this will generate a
    # TypeError exception:

    # bob = Agnostic()
    # express_faith(person=bob)


if __name__ == "__main__":
    main()
