import TCPKit.TCPClient as TCPClient
import struct
import packer


class KeyClient:
    def __init__(self, port):
        self.client = TCPClient.TCPClient("localhost", port, self.handler)

    def handler(self, sock, *args):
        req = struct.pack('I', args[0])
        sock.send(req)

        res = sock.recv(1024)
        pub_n = res[:16]
        pub_e = res[16:]
        pub_key = packer.int_128_unpack(pub_n)
        pub_e = packer.int_32_unpack(pub_e)
        print("[GetPublicKey] PubKey_n: ", pub_key)
        print("[GetPublicKey] PubKey_e: ", pub_e)

        if res != 0:
            result = (pub_key, pub_e)
        else:
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