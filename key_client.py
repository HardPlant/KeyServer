import TCPKit.TCPClient as TCPClient
import struct


class KeyClient:
    def __init__(self, port):
        self.client = TCPClient.TCPClient("localhost", port, self.handler)

    def handler(self, sock, *args):
        req = struct.pack('II', args[0], 0)
        sock.send(req)

        res = sock.recv(1024)
        res, pub_key = struct.unpack('II', res)
        print(res, ',', pub_key)

        if args[0] == res:
            print("[Client] ACK")
            result = pub_key
        else:
            print("[Client] NAK")
            result = -1

        return result

    def get_pubkey(self, id):
        result = []
        self.client.run(id, result)
        return result[0]

if __name__ == '__main__':
    port = 12345
    keyClient = KeyClient(port)

    while True:
        print('ID> ')
        id = int(input())
        pub_key = keyClient.get_pubkey(id)
        print(pub_key)