import datetime
import time

class Packet():
    def __init__(self, _type , data):
        self.type = None            # function code
        self.signal_id = None        # signal id
        self.signal_arg = []        # signal argument list
        self.hex_file = None        # binary data of file125
        self.hex_files = []         # list of binaries of several files
        self.hex_files = []         # details about files
        self.timestamp = round(time.time()*100000)

        if _type == 99:
            self.type = 99
            self.signal_arg = [str(data)]

        elif _type == 10:
            self.type = 10
            self.signal_id = data[0]

            if len(data) > 1:
                self.signal_arg = data[1]


    def __repr__(self):
        if self.type == 99:
            return str(self.signal_arg[0])

        else:
            return str([str(self.type),str(self.signal_id)])