import socket

localIP, localPort  = "127.0.0.1", 6565

TCPclientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCPclientSocket.connect((localIP, localPort))

clientMsg = input("Type your message for the server here: ")
data = bytes(clientMsg, "utf-8")

print("Sending message to {0} port {1}".format(localIP, localPort))
TCPclientSocket.sendall(data)

dataFromServer = str(TCPclientSocket.recv(1024))
print("Message received from the server: ", str(dataFromServer))