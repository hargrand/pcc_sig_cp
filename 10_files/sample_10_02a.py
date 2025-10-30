"""sample_08_03.py - Multiple lines of output to a file"""


def main():
    """Program main function."""
    out_file = open(
        file="lines.txt",
        mode="w",
        encoding="utf-8",
    )
    for line in range(10):
        out_file.write(f"Line {line}\n")
    out_file.close()


if __name__ == "__main__":
    main()
