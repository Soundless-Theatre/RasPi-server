#coding : utf-8
import pyaudio
from socket import socket,AF_INET,SOCK_DGRAM,SOL_SOCKET,SO_BROADCAST
import sys 
from threading import Thread
import time

HOST = ""
PORT = 5008
PORT_t=5007
ADDRESS = "192.168.255.255"
s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
s.bind((HOST,PORT))
f=open("/home/pi/workspace/RasPi-server/title.txt")
title=f.read()
CHUNK = 1024
RATE = 16000
p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16,
                channels = 2,
                rate = RATE,
                frames_per_buffer = CHUNK,
                input = True,
                output = False)

frames=[]
def recaudio():
    while True:
        frames.append(stream.read(CHUNK))
def send():
    while True:
        if len(frames)  > 0:
            s.sendto(frames.pop(),(ADDRESS,PORT))
def send_title():
    global title
    while True:
        time.sleep(9)
        s.sendto(title,(ADDRESS,PORT_t))
if __name__=="__main__":
    p1=Thread(target=recaudio)
    p2=Thread(target=send)
    p1.setDaemon(True)
    p2.setDaemon(True)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    s.close()
    sys.exit()
