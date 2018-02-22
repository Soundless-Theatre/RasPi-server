from socket import *
import sys 
import readaudio
from multiprocessing import Process,Queue

HOST = ""
PORT = 5008
ADDRESS = "192.168.255.255"
s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
s.bind((HOST,PORT))

msg=None

def recaudio(q):
    msg = readaudio.read()
    q.put(msg)
def send():
    global msg,s,ADDRESS,PORT
    s.sendto(msg,(ADDRESS,PORT))
print("hogehgeo")
q=Queue()
p=Process(target=recaudio,args=(q,))
msg=q.get()
p.join()
print("hgoe")
def main():
    global msg
    while True:
        q=Queue()
        p1=Process(target=recaudio,args=(q,))
        p2=Process(target=send)
        msg=q.get()
        p1.join()
        p2.join()
if __name__=="__main__":
    main()
    s.close()
    sys.exit()
