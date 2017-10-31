from socket import *
import sys 
import readaudio
HOST = ""
PORT = 5008
ADDRESS = "192.168.255.255"

s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
s.bind((HOST,PORT))

while True:
    msg = readaudio.read()
    s.sendto(msg,(ADDRESS,PORT))

s.close()
sys.exit()
