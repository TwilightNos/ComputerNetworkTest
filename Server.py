from socket import *

if __name__ == '__main__':
    # 服务器端口
    serverPort = 11000
    #AF_INET代表ipv4协议，SOCK_STREAM代表TCP协议

    listenSocket = socket(AF_INET, SOCK_STREAM)
    # ‘0.0.0.0’ 或者‘’都代表不限连接端口
    listenSocket.bind(('', serverPort))
    # listen中的数字表示最多能够接受几个等待中的服务
    listenSocket.listen(1)
    print('server started at serverPort:'+str(serverPort))
    # True代表无限循环，直到服务器关闭
    connectionSocket, addr = listenSocket.accept()
    print('connected to client')
    while True:
        print('cycle start')
        # 从客户端接收信息
        message = connectionSocket.recv(2048)
        print('message received')
        # 解码接收到的信息并将其变成大写
        capitalizedSentence = message.decode().upper()
        print('message operated')
        # 将处理过后的信息加密后发回给客户端
        connectionSocket.send(capitalizedSentence.encode())
        print('message sent back to client')
        # 输出处理信息的内容
        print('server handled: ' + str(addr) + ' with message:' + message.decode())
        # 如果接收到退出信息则退出循环并关闭服务器
        if capitalizedSentence == 'QUIT' or not capitalizedSentence:
            break

    connectionSocket.close()

