import time
import pickle
from Packet import  Packet
from PySide2.QtNetwork import QTcpSocket, QTcpServer, QHostAddress, QNetworkInterface
from PySide2.QtWidgets import QApplication,QWidget
from PySide2.QtCore import QIODevice, QByteArray, QDataStream, QFile, QThread, Signal, QObject
from PySide2.QtUiTools import QUiLoader
import sys,os
from pathlib import Path


class TCPClient(QTcpSocket):

    def __init__(self,address,port):
        super(TCPClient, self).__init__()

        self.address = address
        self.port = port

        self.readyRead.connect(self.rcv)

    def con(self):
        self.connectToHost(self.address, self.port, QIODevice.ReadWrite)

    def send(self, obj):

        data = pickle.dumps(obj)

        # print(data)
        block = QByteArray()
        out = QDataStream(block, QIODevice.ReadWrite)
        out << QByteArray(data)
        self.write(block)

    def rcv(self):

        data = self.readAll()

        data = data.remove(0, 4)

        obj = pickle.loads(data)

        self.handle_rcv(obj)

    def handle_rcv(self,data):
        print("TCPClient.handle_rcv()")
        print(data)




