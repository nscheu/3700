#!/usr/bin/python -u

class Buffer:

    def __init__(self):
        """
        Initializes a new buffer with size of 1 and an empty
        list of packets.
        :return:
        """
        self.size = 1
        self.packets = []

    def add(self, packet):
        """
        Adds a new packet into the list of packets (does not
        take into account the size, handle that elsewhere)
        :param packet: the packet to add to the buffer (JSON)
        :return:
        """
        self.packets.append(packet)

    def get_top(self):
        """
        Gets the first packet from the buffer, or False if
        the buffer is empty
        :return: JSON packet, or False (if empty)
        """
        if len(self.packets) > 0:
            return self.packets[0]
        else:
            return False

    def remove_top(self):
        """
        Removes the first packet from the buffer
        :return: void - modifies the list of packets
        """
        if len(self.packets):
            self.packets.pop(0)

    def free_slots(self):
        """
        Checks how many free slots are in the buffer
        :return: Boolean - True if there are open slots, else False
        """
        return self.size - len(self.packets) > 0

    def sequence_in_buffer(self, sequence_num):
        """
        checks through the buffer to see if the
        given sequence number is contained on any of the packets
        :param sequence_num: int - the sequence number to find
        :return: True if found, False if doesn't exist
        """
        result = False
        for packet in self.packets:
            if packet['sequence'] == sequence_num:
                return True
        return result

    def insert_packet(self, packet):
        """
        Inserts the given packet into the packet list, in order of
        sequence number (sorted).
        :param packet: the packet to insert
        :return: True if inserted, False if not inserted
        """
        if not len(self.packets):
            self.add(packet)
            return True

        else:
            i = 0
            for curr_pack in self.packets:
                if curr_pack['sequence'] > packet['sequence']:
                    self.packets = self.packets[:i] + [packet] + self.packets[i:]
                    return True
                i += 1
            return False

    def insert_ack_packet(self, packet):
        """
        Inserts the given packet into the packet list, in order of
        ack number (sorted).
        :param packet: the packet to insert
        :return: True if inserted, False if not inserted
        """
        if not len(self.packets):
            self.add(packet)
            return True

        else:
            i = 0
            for curr_pack in self.packets:
                if curr_pack['ack'] > packet['ack']:
                    self.packets = self.packets[:i] + [packet] + self.packets[i:]
                    return True
                i += 1
            return False

