"""sample_08_03.py - Append to the end of a file"""

import time


def main():
    """Program main function."""
    out_file = open(file="timestamps.txt", mode="a", encoding="utf-8")
    ts = time.localtime()
    out_file.write(
        f"{ts.tm_year}-"
        f"{ts.tm_mon:02}-"
        f"{ts.tm_mday:02} "
        f"{ts.tm_hour:02}:"
        f"{ts.tm_min:02}:"
        f"{ts.tm_sec:02}\n"
    )
    out_file.close()


if __name__ == "__main__":
    main()
