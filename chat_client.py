import TCPKit.TCPClient as TCPClient

class ChatClient:
    def __init__(self, port):
        self.client = TCPClient.TCPClient("localhost", port, self.handler)

    def handler(self, sock, *args):
        msg = args[0]
        req = bytes(msg, 'UTF-8')
        sock.send(req)

    def sendMessage(self, msg):
        self.client.run(msg)


if __name__ == '__main__':
    port = 12345
    ChatClient = ChatClient(port)

    while True:
        print('Send Message> ')
        msg = input()
        keyClient.
        print(pub_key)