import TCPKit.TCPClient as TCPClient

class ChatClient:
    def __init__(self, port):
        self.client = TCPClient.TCPClient("localhost", port, self.handler)

    def handler(self, sock, *args):
        msg = args[0]
        req = bytes(msg, 'UTF-8')
        sock.send(req)

    def send_message(self, msg):
        result = []
        self.client.run(msg, result)


if __name__ == '__main__':
    port = 12345
    chatClient = ChatClient(port)

    while True:
        print('Send> ', end='')
        msg = input()
        chatClient.send_message(msg)
