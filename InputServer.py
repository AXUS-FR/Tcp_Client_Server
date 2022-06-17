from server import TCPServer

class InputServer(TCPServer):

    def __init__(self, address, port, parent = None):
        TCPServer.__init__(self, address, port, parent)

    def handle_request(self,packet):
        print("InputServer.handle_request()")
        print(packet)

        self.handle_answer(packet)

    def handle_answer(self,packet):
        print("InputServer.handle_answer()")
        self.send_packet(packet.type, [packet.signal_id])

