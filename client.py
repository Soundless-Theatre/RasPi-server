import socket

server_address = ('localhost', 6789)
max_size = 4096

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto(b'Don\'t!', server_address)

data, server = client.recvfrom(max_size)

print('received message:', data)
client.close()
