import datetime
import time

class Packet():
    def __init__(self, _type , data):
        self.type = None            # function code
        self.signal_id = None        # signal id
        self.signal_arg = []        # signal argument list
        # self.hex_file = None        # binary data of file
        self.hex_files_bytes = []         # list of binaries of several files
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

    def wrap_table(self,table,name):
        self.type = 20
        self.signal_arg = [name,table]

    def wrap_input_table(self, table):
        self.signal_id = 104
        self.wrap_table(table,"input")

    def wrap_file(self,path):
        self.type = 30
        self.hex_files.append(path)

        file = open(path, "rb")
        file_bytes = file.read()
        self.hex_files_bytes.append(file_bytes)
        file.close

    def wrap_picture(self,path):
        self.wrap_file(path)
        self.signal_id = 105

    def unwrap_file(self, newname = None):

        print("Packet.unwrap_file()")
        if self.type == 30:

            if newname == None:
                path = self.hex_files[0]
            else:
                print(newname)
                path = newname

            file = open(path,"wb")
            file.write(self.hex_files_bytes[0])

