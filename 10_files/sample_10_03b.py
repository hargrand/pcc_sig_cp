"""sample_08_03.py - Multiple lines of output to a file"""


def main():
    """Program main function."""
    in_file = open(
        file="timestamps.txt",
        mode="r",
        encoding="utf-8",
    )

    lines = in_file.readlines()
    in_file.close()

    for line in lines:
        print(line, end="")


if __name__ == "__main__":
    main()
