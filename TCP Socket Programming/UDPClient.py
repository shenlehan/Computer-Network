from socket import *

if __name__ == '__main__':
    serverName = '10.4.153.13' # 或者采用回环ip地址'127.0.0.1'，指向本机
    serverPort = 12000
    clineSocket = socket(AF_INET, SOCK_DGRAM)
    message = input('Input lowercase sentence:')
    clineSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAddress = clineSocket.recvfrom(2048)
    print(modifiedMessage.decode())
    clineSocket.close()