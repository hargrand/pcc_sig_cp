"""activity_09_01.py - Shows usage of the vector class"""

import vector


def main():
    """Main function of the program"""
    v1 = vector.Vector(3, 4)
    v2 = vector.Vector(5, 6)
    v3 = v1 + v2
    v4 = v1 - v2

    print(f"v1 = {v1} / v1.length = {v1.length()} / v1.direction = {v1.direction()}")
    print(f"v2 = {v2} / v2.length = {v2.length()} / v2.direction = {v2.direction()}")
    print(f"v3 = {v3} / v3.length = {v3.length()} / v3.direction = {v3.direction()}")
    print(f"v4 = {v4} / v4.length = {v4.length()} / v4.direction = {v4.direction()}")


if __name__ == "__main__":
    main()
