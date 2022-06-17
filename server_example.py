import time
from Packet import  Packet
import pickle

from PySide2.QtNetwork import QTcpSocket, QTcpServer, QHostAddress, QNetworkInterface
from PySide2.QtWidgets import QApplication,QWidget
from PySide2.QtCore import QFile, QThread, QObject, Signal, QIODevice,QByteArray,QDataStream
import sys

from InputServer import InputServer


class Win(QWidget):

    def __init__(self):
        super(Win, self).__init__()

        self.server = InputServer("192.168.1.12",5050,self)


if __name__ == "__main__":
    app = QApplication([])

    window = Win()

    window.show()

    sys.exit(app.exec_())