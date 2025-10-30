"""sample_08_03.py - Append to the end of a file"""

import struct


def main():
    """Program main function."""

    in_file = open(file="binary.bin", mode="rb")
    byte_array = in_file.read()
    in_file.close()

    unpacked_value = struct.unpack("d", byte_array)[0]
    print(unpacked_value)


if __name__ == "__main__":
    main()
