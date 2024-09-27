import socket

serverAddressPort = ("127.0.0.1", 6565)
bytesToSend = 'Message received.'

TCPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

TCPServerSocket.bind(serverAddressPort)
print("Server up and running.")

TCPServerSocket.listen(10)
msg, adress = TCPServerSocket.accept()

while 1:
    dataFromClient = msg.recv(1024)
    msg.sendall(dataFromClient)
