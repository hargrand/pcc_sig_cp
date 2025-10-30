"""activity_12_01.py - Read a file and count the occurrences of each word"""

from pathlib import Path
import pprint


FILE_PATH = Path(__file__).resolve().parent
DOCUMENT = FILE_PATH / "philemon_esv.txt"


def read_document(file_name: str) -> list[str]:
    """Read a document containing only words separated by spaces without any punctuation"""
    with open(file=file_name, mode="r", encoding="utf-8") as file:
        content = file.read()

    return content.upper().split(" ")


def get_unique_words(words: list[str]) -> set[str]:
    """Given a list of words return a set of unique words in the list"""
    return set(words)


def get_word_count(words: list[str]) -> dict[str, int]:
    """Compute the word count for each word in the list"""
    return {x: words.count(x) for x in get_unique_words(words)}


def count_words_in_file(file_name: str) -> dict[str, int]:
    """Compute the word count for each word in the document"""
    return get_word_count(words=read_document(file_name=file_name))


def main():
    """Read content of the file and return the word count"""
    print(f"THe file path is {FILE_PATH}")
    print(f"The word count in the file {DOCUMENT} is:")
    pprint.pprint(count_words_in_file(DOCUMENT))


if __name__ == "__main__":
    main()
