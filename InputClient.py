from client import TCPClient
from Packet import Packet
from PySide2.QtCore import Signal

import time

class InputClient(TCPClient):

    input_table_rcv = Signal()
    picture_rcv = Signal()

    def __init__(self,address,port):
        TCPClient.__init__(self,address,port)

        self.state = None

    def send_packet(self,a,b):
        data = Packet(a, b)
        self.send(data)




    def handle_rcv(self,packet):
        print("InputClient.handle_rcv()")
        # print(packet)
        print("----")
        print(packet.type)
        print(packet.signal_id)
        print(self.state)
        print(packet)


        print("----")

        if packet.type == 10:

            if packet.signal_id == 101 and self.state == 101:

                self.state = None
                # print("load action confirm")

        if packet.type == 30:

            if packet.signal_id == 105 and self.state == 105:

                # --------------------- ONLY FOR TEST, NEED TO IMPLEMENT ---------------

                path = (str(time.time()).split(".")[0]) + ".PNG"

                packet.unwrap_file(path)

                # ---------------------------------------------------------------------




    def load_action(self):
        self.send_packet(10, [101])
        self.state = 101

    def get_picture(self):

        packet = Packet(0,[0])
        packet.type = 10
        packet.signal_id = 105
        packet.signal_arg = [1,1]

        self.send(packet)
        self.state = 105






