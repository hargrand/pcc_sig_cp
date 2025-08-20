"""sample_08_03.py - Append to the end of a file"""

import struct
import math


def main():
    """Program main function."""
    packed_bytes = struct.pack("d", math.pi)
    byte_array = bytearray(packed_bytes)

    out_file = open(file="binary.bin", mode="wb")
    out_file.write(byte_array)
    out_file.close()


if __name__ == "__main__":
    main()
