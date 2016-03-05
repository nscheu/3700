#!/usr/bin/python -u

class Buffer:

    def __init__(self, size=1):
        self.size = size
        self.packets = []

    def add(self, packet):
        if len(self.packets) < self.size:
            self.packets.append(packet)
            return True
        else:
            return False
