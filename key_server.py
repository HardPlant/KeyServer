from TCPKit import TCPServer
import struct

class KeyServer:
    def __init__(self, port):
        self.port = port
        self.queue = []
        self.pubkey = []

    def routine(self, sock):
        recv = sock.recv(1024)
        id, _ = struct.unpack('II', recv)
        req = -1
        try:
            index = self.queue.index(id)
            req = self.pubkey[index]
            print("id: ",id, "pubkey: ", req, "served.")
            req = struct.pack("II", id,req)
        except ValueError:
            print("id: ", id)
            print("Key Not Found")
            req = struct.pack("II", 0, 0)
        finally:
            req = bytes(req)
            sock.send(req)

    def register(self, id, public_key):
        self.queue.append(id)
        self.pubkey.append(public_key)

    def serve_public(self):
        print("Server Running at port %d" % self.port)
        server = TCPServer.TCPServer(self.port, self.routine)
        server.serve_forever()


def get_yes_or_no(msg):
    while True:
        print(msg)
        ans = input()
        if ans.lower() == 'y':
            return True
        if ans.lower() == 'n':
            return False


if __name__ == '__main__':
    keyServer = KeyServer(12345)
    while get_yes_or_no("공개키를 등록하시겠습니까?"): # Register Status
        print("등록할 아이디를 입력하십시오: ")
        id = int(input())
        print("등록할 공개키를 입력하십시오: ")
        pubkey = int(input())
        keyServer.register(id,pubkey)

    keyServer.serve_public()