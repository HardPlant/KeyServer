import socket

class KeyServer:
    def __init__(self):
        self.sock = socket.socket()
        pass

    def register(self,public_key):
        pass

    def serve_public(self):
        sock = self.sock
        recv = sock.recv(1024)
        req = int(recv)

class KeyProtocol:
    def __init__(self, sock, id):
        self.sock = sock
        self.id = id

    def init(self):
        pass

    def register(self):
        pass

    def get_public_key(self, id):
        req = id
        return req
def get_yes_or_no():
    pass

if __name__ == '__main__':
    keyServer = KeyServer()
    while(True): # Register Status
        print("등록할 아이디를 입력하십시오: ")
        id = input()
        print("등록할 공개키를 입력하십시오: ")
        pubkey = input()
        keyServer.register(keyServer,id,pubkey)

    while(True): # Serve
        keyServer.init()