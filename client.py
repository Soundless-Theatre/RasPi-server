from socket import *
import sys

HOST = ""
PORT = 5008
ADDRESS = "192.168.255.255"

s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
s.bind((HOST,PORT))

while True:
    msg = bytes(b'hoge')
    s.sendto(msg,(ADDRESS,PORT))
    if msg == ".":
        break

s.close()
sys.exit()
