"""sample_08_01a.py - Basic file output"""


def main():
    """Program main function."""
    out_file = open(
        file="file.txt",
        mode="w",
        encoding="utf-8",
    )
    out_file.write("Hello World!")
    out_file.close()


if __name__ == "__main__":
    main()
