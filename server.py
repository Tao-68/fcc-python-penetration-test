import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

serversocket.bind((host, port))
serversocket.listen()

while True:
    clientsocket, address = serversocket.accept()

    print("Received connection from %s" % str(address))

    message = 'Hello from the other side!' + "\r\n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()