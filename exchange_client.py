import TCPKit.TCPClient as TCPClient
import rsa
import packer


class ExchangeClient:
    def __init__(self, port, pub):
        self.client = TCPClient.TCPClient("localhost", port, self.handler)
        self.pub = pub

    def handler(self, sock, *args):
        msg = args[0]
        packed = packer.int_32_pack(msg)
        print("[ExchangeClient] encrypt with that_pub..")
        req = rsa.encrypt(packed, self.pub)
        sock.send(req)

    def send_message(self, msg):
        result = []
        self.client.run(msg, result)


if __name__ == '__main__':
    print("Enter Bob's Public.n:")
    n = int(input())
    print("Enter Bob's Public.e:")
    e = int(input())
    pub = rsa.PublicKey(n,e)

    port = 12345
    chatClient = ExchangeClient(port, pub)

    print('Send> ', end='')
    msg = int(input())
    chatClient.send_message(msg)
