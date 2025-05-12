import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
addr = socket.gethostbyname(host)
port = 444

clientsocket.connect((addr, port))

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))