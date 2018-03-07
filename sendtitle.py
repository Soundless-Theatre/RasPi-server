#coding : utf-8
from socket import socket,AF_INET,SOCK_DGRAM,SOL_SOCKET,SO_BROADCAST
import time
HOST = ""
PORT=5007
ADDRESS = "192.168.255.255"
s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
s.bind((HOST,PORT))
f=open("/home/pi/workspace/RasPi-server/title.txt")
title=f.read()
f.close()
while True:
    time.sleep(9)
    s.sendto(title,(ADDRESS,PORT))
