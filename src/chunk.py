class Chunk:
    def __init__(self, length, chunk_type, crc):
        self.length = length
        self.chunk_type = chunk_type
        self.crc = crc

    def print_basic_info(self):
        print("Type: {type}".format(type=self.chunk_type))
        print("Length: {length} bytes".format(length=self.length))
        print("CRC: {crc}".format(crc=self.crc))

    # TODO: implement this
    def show_details(self):
        print("To be implemented\n")
