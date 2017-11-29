from TCPKit import TCPServer


class KeyServer:
    def __init__(self, port):
        self.port = port
        self.queue = []
        self.pubkey = []

    def routine(self, sock):
        recv = sock.recv(1024)
        req = -1
        try:
            index = self.queue.index(int(recv))
            req = index
        except ValueError:
            pass
        finally:
            sock.send(req)

    def register(self, id, public_key):
        self.queue.append(id)
        self.pubkey.append(public_key)

    def serve_public(self):
        server = TCPServer.TCPServer(self.port, self.routine)


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
        id = input()
        print("등록할 공개키를 입력하십시오: ")
        pubkey = input()
        keyServer.register(id,pubkey)

    keyServer.serve_public()