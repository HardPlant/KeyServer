import TCPKit.TCPClient as TCPClient

def handler(socket, msg, *args):
    socket.send(bytes(msg,'UTF-8'))
    msg = socket.recv(1024)
    print(msg.decode())


if __name__ == '__main__':
    client = TCPClient.TCPClient("localhost", 12345, handler)
    while True:
        result = []
        print('> ')
        msg = input()
        client.run(msg, result)

