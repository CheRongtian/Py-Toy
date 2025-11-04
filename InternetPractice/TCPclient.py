from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM) 
# create TCP socket for server, remote port 12000
clientSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
# No need to attach server name, port
print('From Server; ', modifiedSentence.decode())
clientSocket.close()