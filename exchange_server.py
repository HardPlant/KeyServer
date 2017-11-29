from TCPKit import TCPServer
import rsa
import struct

class ChatServer:
    def __init__(self, port, sym):
        self.port = port
        self.queue = []
        self.pubkey = []
        self.sym = sym

    def routine(self, sock):
        recv = sock.recv(1024)
        msg = recv.decode()
        print("Recv> " , msg, end='')

    def serve(self):
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
    (pub, pri) = rsa.newkeys(32)
    print("Public.n: ", pub.n)
    print("Public.e: ", pub.e)

    chatServer = ChatServer(12345)
    chatServer.serve()