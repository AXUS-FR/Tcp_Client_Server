from client import TCPClient

from InputClient import InputClient

import time
import pickle
from Packet import  Packet
from PySide2.QtNetwork import QTcpSocket, QTcpServer, QHostAddress, QNetworkInterface
from PySide2.QtWidgets import QApplication,QWidget
from PySide2.QtCore import QIODevice, QByteArray, QDataStream, QFile, QThread, Signal, QObject
from PySide2.QtUiTools import QUiLoader
import sys,os
from pathlib import Path


class Loop(QThread):

    def __init__(self):
        super(Loop,self).__init__()

    def run(self):
        while True:
            print("loop")
            time.sleep(1)


class Win(QWidget):

    def __init__(self, _client):
        super(Win, self).__init__()
        self.setWindowTitle("TCP Client")
        self.client = _client

        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "client.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)

        ui_file.close()

        self.ui.button.clicked.connect(self.send)
        self.ui.button_raw.clicked.connect(self.send_raw)

        self.ui.b1.clicked.connect(self.client.load_action)
        self.ui.b2.clicked.connect(self.client.get_picture)



    def send(self):
        # data = self.ui.line.text()

        data = Packet(10, [101])

        self.client.send(data)

    def send_raw(self):
        data = bytes(self.ui.line.text(), 'utf-8')
        self.client.send(data)


if __name__ == "__main__":
    app = QApplication([])

    client = InputClient("192.168.1.12", 5050)

    client.con()

    window = Win(client)
    #
    # loop = Loop()
    # loop.start()

    window.show()

    sys.exit(app.exec_())