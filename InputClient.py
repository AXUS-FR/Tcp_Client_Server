from client import TCPClient
from Packet import Packet
from PySide2.QtCore import Signal

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
        print(packet)

        if packet.type == 10:

            if packet.signal_id == 101 and self.state == 101:

                self.state = None
                print("load action confirm")


    def load_action(self):
        self.send_packet(10, [101])
        self.state = 101




