import pickle
from Packet import Packet

from PySide2.QtCore import QByteArray, QDataStream, QIODevice

b = bytes("string",'utf-8')

ba = QByteArray(b)

out = QDataStream(ba, QIODevice.ReadWrite)

ob = QByteArray()

ob = out.writeRawData(out)

print(b)
print(ba)


print (ob)

