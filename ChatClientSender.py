SERVER_ADDRESS_PORT = ("127.0.0.1", 4353)
MAX_MSG_SIZE = 2048
MSG_SIZE = 1024


import sys

from socket import *

s = socket(AF_INET, SOCK_DGRAM)
file_name = sys.argv[1]

f = open(file_name, "rb")
data = f.read(MSG_SIZE)
s.sendto("NAME sender".encode(), SERVER_ADDRESS_PORT)
s.sendto("CONN receiver".encode(), SERVER_ADDRESS_PORT)
while (data):
    if (s.sendto(data, SERVER_ADDRESS_PORT)):
        print("sending ...")
        data = f.read(MSG_SIZE)
s.close()
f.close()
