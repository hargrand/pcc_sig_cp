"""sample_08_02.py - Basic file input"""


def main():
    """Program main function."""
    in_file = open(
        file="file.txt",
        mode="r",
        encoding="utf-8",
    )
    text = in_file.read()
    print(text)
    in_file.close()


if __name__ == "__main__":
    main()
