"""sample_08_03.py - Multiple lines of output to a file"""


def main():
    """Program main function."""
    with open(file="timestamps.txt", mode="r", encoding="utf-8") as in_file:
        lines = in_file.readlines()

    for line in lines:
        print(line, end="")


if __name__ == "__main__":
    main()
