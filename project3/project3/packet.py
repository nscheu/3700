#!/usr/bin/python -u

from struct import pack, unpack

class Packet:

    def __init__(self, id_in, sequence_number, data):
        self.max_size = 1460
        self.header_size = 20
        self.payload_max_size = self.max_size - self.header_size

        self.id = id_in
        self.sequence_number = sequence_number
        self.data = data


    #def package_into_binary(self):
    #    return pack(self, bytes)
