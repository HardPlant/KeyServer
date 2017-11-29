from chat_client import ChatClient
from chat_server import ChatServer
from exchange_server import ExchangeServer
from exchange_client import ExchangeClient
from key_client import KeyClient
import threading
import rsa


def chat_server_thread(port,sym_key):
    chat_server = ChatServer(port, sym_key)
    chat_server.serve()

def chat_client_thread(port, sym_key):
    chat_client = ChatClient(port, sym_key)
    while True:
        print('Send Message> ')
        msg = input()
        chat_client.send_message(msg)

def phase_init_server_and_client():
    print("채팅 서버 포트를 입력하세요: ")
    serve_port = int(input())
    server = threading.Thread(target=chat_server_thread
                              ,args=(serve_port,))
    server.start()

    print("접속할 포트를 입력하세요: ")
    dest_port = int(input())
    client = threading.Thread(target=chat_client_thread
                              ,args=(dest_port,))
    client.start()

def phase_get_key():
    key_client = KeyClient(34567)
    while True:
        print("상대 서버 id를 입력하세요: ")
        that_id = int(input())
        that_pubkey = key_client.get_pubkey(that_id)
        print("결과: ", that_pubkey, 'type:', type(that_pubkey))
        if that_pubkey != -1:
            break
        print("잘못된 id입니다.")

    print("상대의 공개키: ", that_pubkey)

    return that_pubkey

def phase_exchange_sym_key(that_key):
    pass


def phase_chat(sym_key):
    pass

if __name__ == '__main__':
    (pub, pri) = rsa.newkeys(128)
    print("Public: ", pub)

    phase_init_server_and_client()
    that_key = phase_get_key()
    sym_key = phase_exchange_sym_key(that_key)
    phase_chat(sym_key)


