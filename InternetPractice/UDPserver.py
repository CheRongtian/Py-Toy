from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM) # create UDP socket
serverSocket.bind(('', serverPort)) # bind socket to local port number 12000
print("The server is ready to receive")
while True: # loop forever
    message, clientAddress = serverSocket.recvfrom(2048) 
    # Read from UDP socket into message, getting client's address (client IP and port)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    # seng upper case string back to this client