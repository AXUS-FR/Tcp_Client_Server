import time
from Packet import  Packet
import pickle

from PySide2.QtNetwork import QTcpSocket, QTcpServer, QHostAddress, QNetworkInterface
from PySide2.QtWidgets import QApplication,QWidget
from PySide2.QtCore import QFile, QThread, QObject, Signal, QIODevice,QByteArray,QDataStream
import sys

class TCPServer(QTcpServer):
    clientReadyToRead = Signal()
    clientDisconnected = Signal()

    def __init__(self, address, port, parent = None):
        QTcpServer.__init__(self,parent)
        self.address = address
        self.port = port
        self.socket = self.makeSocket()
        self.state = None

        self.open_connexion()

    def makeSocket(self):
        socket = QTcpSocket(self)
        socket.readyRead.connect(self.onSocketReadyRead)
        socket.disconnected.connect(self.clientDisconnected)
        return socket

    def open_connexion(self):

        if self.listen(QHostAddress(self.address), self.port):
            print("server is listening")
        else:
            print("error during listening process")

    def incomingConnection(self, socketDescriptor):
        print("connexion is incoming...")
        self.socket.setSocketDescriptor(socketDescriptor)

    def onSocketReadyRead(self):
        data = self.socket.readAll()
        data = data.remove(0,4)

        packet = pickle.loads(data)
        self.handle_request(packet)

    def send(self, obj):
        data = pickle.dumps(obj)

        block = QByteArray()
        out = QDataStream(block, QIODevice.ReadWrite)
        out << QByteArray(data)
        self.socket.write(block)

    def send_packet(self,a,b):
        data = Packet(a, b)
        self.send(data)

    def handle_request(self,packet):
        print("TCPServer.handle_request()")
        print(packet)

        self.handle_answer(packet)

    def handle_answer(self,packet):
        print("TCPServer.handle_answer()")
        self.send_packet(packet.type, [packet.signal_id])






