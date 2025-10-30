"""activity_10_01.py - A program that creates a copy of itself"""

import os


def main():
    """The main function"""
    infilename = os.path.abspath(__file__)
    print(infilename)

    with open(file=infilename, mode="r", encoding="utf-8") as infile:
        lines = infile.readlines()

    outfilename = infilename + ".copy"
    with open(file=outfilename, mode="w", encoding="utf-8") as outfile:
        for line in lines:
            outfile.write(line)

    print(f"{outfilename} was created")
    print(f"It contains {len(lines)} lines")
    character_count = 0
    for line in lines:
        character_count += len(line)
    print(f"It contains {character_count} characters")
    print(
        f"It contains an average of {character_count / len(lines)} characters per line"
    )


if __name__ == "__main__":
    main()
