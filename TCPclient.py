from socket import *


if __name__ == '__main__':
    # 必须是localhost（为什么？）
    serverName = '54.227.184.239'
    # serverPort 一定要和server的serverPort数字一致，否则无法建立连接
    serverPort = 11000
    #AF_INET代表ipv4协议，SOCK_STREAM代表TCP协议
    clientSocket = socket(AF_INET,SOCK_STREAM)
    #与服务器建立连接
    clientSocket.connect((serverName,serverPort))
    # 输入要发送给服务器的信息
    while True:
        message = input('Input sentence:')
        # 将编码后的信息发送给服务器
        clientSocket.send(message.encode())
        print('message sent')
        # 接受从服务器发回的信息
        modifiedSentense = clientSocket.recv(2048)
        print('message received')
        receivedMessage = modifiedSentense.decode()
        if receivedMessage == 'QUIT' or not receivedMessage:
            break
        # 将从服务器收到的信息解码并输出
        print('From Server:' + receivedMessage)
        # 关闭服务器
    clientSocket.close()