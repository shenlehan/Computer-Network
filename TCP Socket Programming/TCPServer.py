from socket import *

if __name__ == '__main__':
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1) # get ready to receive the connetion request from the client
    print('The server is ready to receive')

    while True:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024).decode()
        captalizedSentence = sentence.upper()
        connectionSocket.send(captalizedSentence.encode())
        connectionSocket.close()