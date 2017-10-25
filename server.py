import socket

server_address = ('localhost', 6789)
max_size = 4096

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_address)

data, client = server.recvfrom(max_size)

print('received message:', data)
server.sendto(b'I want to drink monster...', client)
server.close()
