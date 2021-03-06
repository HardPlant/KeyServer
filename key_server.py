from TCPKit import TCPServer
import struct
import packer

class KeyServer:
    def __init__(self, port):
        self.port = port
        self.queue = []
        self.pubkey = []
        self.pub_e = []

    def routine(self, sock):
        self.serve_n(sock)

    def serve_n(self, sock):
        recv = sock.recv(1024)
        id = struct.unpack('I', recv)[0]
        res = packer.int_128_pack(0)
        try:
            index = self.queue.index(id)
            req = self.pubkey[index]
            req_e = self.pub_e[index]
            print("id: ",id, "pubkey: ", req, "served.")
            res_n = packer.int_128_pack(req)
            res_e = packer.int_32_pack(req_e)
            print("RES_N:" ,res_n)
            print("RES_E:" ,res_e)
            res = res_n + res_e

        except ValueError:
            print("id: ", id)
            print("Key Not Found")
        finally:
            print("RES:" ,res)
            sock.send(res)


    def register(self, id, public_key, e):
        self.queue.append(id)
        self.pubkey.append(public_key)
        self.pub_e.append(e)

    def serve_public(self):
        print("Server Running at port %d" % self.port)
        server = TCPServer.TCPServer(self.port, self.routine)
        server.serve_forever()


def get_yes_or_no(msg):
    while True:
        print(msg, end='')
        ans = input()
        if ans.lower() == 'y':
            return True
        if ans.lower() == 'n':
            return False


if __name__ == '__main__':
    print("키서버 포트: ", end='')
    port = int(input())
    keyServer = KeyServer(port)
    pubkey_1 = 202137387733458537301164105994247647661
    pubkey_2 = 228824876101654018166397806380867770343
    '''
    while get_yes_or_no("공개키를 등록하시겠습니까?"): # Register Status
        print("등록할 아이디를 입력하십시오: ", end='')
        id = int(input())
        print("등록할 공개키의 n값를 입력하십시오: ", end='')
        pubkey_n = int(input())
        print("등록할 공개키의 e값를 입력하십시오: ", end='')
        pubkey_e = int(input())
        keyServer.register(id,pubkey_n, pubkey_e)
    '''
    keyServer.register(1,pubkey_1, 65537)
    keyServer.register(2,pubkey_2, 65537)

    print(pubkey_1, "이 등록되었습니다.")
    print(pubkey_2, "이 등록되었습니다.")


    keyServer.serve_public()