from socket import *
import sys 
import readaudio
from multiprocessing import Pool

HOST = ""
PORT = 5008
ADDRESS = "192.168.255.255"
s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
s.bind((HOST,PORT))

msg=None
def recaudio():
    global msg
    msg = readaudio.read()
def send():
    global msg
    s.sendto(msg,(ADDRESS,PORT))
while True:
    recaudio()
    send()

s.close()
sys.exit()
