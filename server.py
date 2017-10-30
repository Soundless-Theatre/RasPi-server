from socket import *
import sys

HOST = ""
PORT = 5008

s = socket(AF_INET,SOCK_DGRAM)
s.bind((HOST,PORT))

while True:
    msg, address = s.recvfrom(8192)
    if msg == ".":
        print("Sender is closed")
        break
    
    print("message:",msg,"from",address)

s.close()
sys.exit()
