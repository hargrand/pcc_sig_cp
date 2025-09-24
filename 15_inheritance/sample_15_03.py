"""sample_15_03.py - Multiple inheritance."""


class Vegetarian:
    """Defines something that eats vegetables"""

    def __init__(self, favorite):
        self._favorite_vegetable = favorite

    def favorite_vegetable(self):
        """What's on the outside"""
        print(f"Favorite vegetable: {self._favorite_vegetable}")


class Carnivore:
    """Defines something that eats meats"""

    def __init__(self, favorite):
        self._favorite_meat = favorite

    def favorite_meat(self):
        """This is how we travel in an automobile"""
        print(f"Favorite meat: {self._favorite_meat}")


class Omnivore(Vegetarian, Carnivore):
    """Defines something that eats both meat and vegetables"""

    def __init__(self, vegetable, meat):
        Vegetarian.__init__(self, vegetable)
        Carnivore.__init__(self, meat)

    def favorite_foods(self):
        """Display favorite foods of the omnivore"""
        self.favorite_vegetable()
        self.favorite_meat()


def main():
    "Main function for the program"
    racoon = Omnivore("cuccumbers", "snake")
    racoon.favorite_foods()


if __name__ == "__main__":
    main()
