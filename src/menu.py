import signature
from ihdr import IHDR
from plte import PLTE
from chunk_data import *


# name, size, tmp = load_data("png_files/duze.png")
# file_info(name, size)

def menu():
    with open("../img-example/sjpNp.png", "rb") as f:  # open file
        byte_string = f.read()  # read all of its data bytes
        if not signature.check_signature(byte_string):
            print("Not a PNG file")
            exit(1)
        f.close()  # close file

        length, data, crc = parse_data(byte_string, b"IHDR")
        test_IHDR = IHDR(length, data, crc)
        test_IHDR.print_info()

        length, data, crc = parse_data(byte_string, b"PLTE")
        test_PLTE = PLTE(length, data, crc, test_IHDR.color_type)
        test_PLTE.print_info()
