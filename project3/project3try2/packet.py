#!/usr/bin/python -u

from struct import pack, unpack
import random
import json

class Packet:

    def __init__(self, sequence_number, data, id_in=int(random.random() * 1000), ack=0, eof=0):
        self.max_size = 1460
        self.header_size = 20
        self.payload_max_size = self.max_size - self.header_size

        self.id = id_in
        self.sequence_number = sequence_number
        self.data = data
        self.ack = ack
        self.eof = eof

    def package(self):
        return json.dumps('{"id": ' + str(self.id) +
                          ', "sequence": ' + str(self.sequence_number) +
                          ', "data": ' + str(self.data) +
                          ', "ack" :' + str(self.ack) +
                          ', "eof": ' + str(self.eof) + '}')


    #def package_into_binary(self):
    #    return pack(self, bytes)

def create_package_from_json(json_message):
    return Packet(json_message["sequence"], json_message["data"], json_message["id"], json_message["ack"], json_message["eof"])
