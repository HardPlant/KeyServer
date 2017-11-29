from TCPKit import TCPServer
import rsa
import packer

class ExchangeServer:
    def __init__(self, port, pri):
        self.port = port
        self.queue = []
        self.pubkey = []
        self.pri = pri

    def routine(self, sock):
        recv = sock.recv(1024)
        print("[ExchangeServer] decrypt with pri..")
        msg = rsa.decrypt(recv,self.pri)
        unpacked_msg = packer.int_32_unpack(msg)
        print("Recv> " , unpacked_msg)
        return unpacked_msg

    def serve(self):
        print("Server Running at port %d" % self.port)
        server = TCPServer.TCPServer(self.port, self.routine)
        return server.serve_once()


def get_yes_or_no(msg):
    while True:
        print(msg)
        ans = input()
        if ans.lower() == 'y':
            return True
        if ans.lower() == 'n':
            return False


if __name__ == '__main__':
    (pub, pri) = rsa.newkeys(128)
    print("Public.n: ", pub)
    print("Public.e: ", pri)

    chatServer = ExchangeServer(12345, pri)
    key = chatServer.serve()
    print("SymKey : ", key)
