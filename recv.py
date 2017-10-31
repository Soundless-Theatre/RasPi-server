from socket import *
import sys 
import playaudio
HOST = ""
PORT = 5008

s = socket(AF_INET,SOCK_DGRAM)
s.bind((HOST,PORT))

while True:
   msg, address = s.recvfrom(8192)
   playaudio.play(msg)

s.close()
sys.exit()
