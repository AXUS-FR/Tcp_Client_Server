from server import TCPServer
from PySide2.QtCore import Signal
from Packet import Packet

"""
Connect details:

    load_action_A signal is emited when user push load button on HMI side
    => load_action_B() slot might to be triggered by SFJob on load_action_A receipt

    hide_A signal is emited when user push hide Bar button on HMI side
    => get_input_B() slot might to be triggered by SFJob on hide_A receipt after hiding the bar
    
    
    hide_job_A signal is emited when user push hide job button on HMI side
    => get_input_B() slot might to be triggered by SFJob on hide_A receipt after hiding the job
    
    get_input_A signal is emited when client ask for input table update
    => get_input_B() slot might to be triggered by SFJob on get_input_A receipt
    
    get_picture_A signal is emited when client ask for picture send
    => get_picture_B() slot might to be triggered by SFJob on get_picture_A receipt


"""

class InputServer(TCPServer):

    load_action_A = Signal()
    hide_A = Signal()
    hide_job_A = Signal()
    get_input_A = Signal()
    get_picture_A = Signal()

    def __init__(self, address, port, parent = None):
        TCPServer.__init__(self, address, port, parent)

    def handle_request(self,packet):
        print("InputServer.handle_request()")

        if packet.type == 10:

            if packet.signal_id == 101:
                self.state = 101
                self.load_action_A.emit()


            elif packet.signal_id == 102:
                job_id = packet.signal_arg[0]
                bar_id = packet.signal_arg[1]
                self.state = 102
                self.hide_A.emit(job_id,bar_id)

            elif packet.signal_id == 103:
                job_id = packet.signal_arg[0]
                self.state = 103
                self.hide_job_A.emit(job_id)

            elif packet.signal_id == 104:
                self.state = 104
                self.get_input_A.emit()

            elif packet.signal_id == 105:
                maker = packet.signal_arg[0]
                ref = packet.signal_arg[1]
                self.state = 105
                self.get_picture_A.emit(maker, ref)

            else:  # ----- return packet in case we don't handle
                self.handle_answer(packet)

    def handle_answer(self,packet):
        print("InputServer.handle_answer()")
        self.send_packet(packet)

    def load_action_B(self):
        if self.state == 101:

            self.state = None
            self.send_packet(10, [101])
        else:
            print("load_action_A is not pending on server side")

    def get_input_B(self, packet=Packet(0,[0])):
        if self.state == 102 or self.state == 103 or self.state == 104:

            self.state = None
            self.send_packet(packet)
        else:
            print("server is not waiting for input table update")

    def get_picture_B(self, packet=Packet(0, [0])):
        if self.state == 105:

            self.state = None
            self.send_packet(packet)
        else:
            print("server is not waiting for picture send")