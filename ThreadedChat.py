from chat_client import ChatClient
from chat_server import ChatServer
from exchange_server import ExchangeServer
from exchange_client import ExchangeClient
from key_client import KeyClient
import packer
import threading
import rsa

def chat_client_gen_sym_key():
    return 65537

def chat_server_thread(port, pri):
    exchange_server = ExchangeServer(port, pri)
    sym_key = exchange_server.serve()

    chat_server = ChatServer(port, sym_key)
    chat_server.serve()

def chat_client_thread(port, pub):
    exchange_client = ExchangeClient(port, pub)
    sym_key = chat_client_gen_sym_key()
    exchange_client.send_message(sym_key)

    chat_client = ChatClient(port, sym_key)
    while True:
        print('Send Message> ')
        msg = input()
        chat_client.send_message(msg)

def phase_init_server_and_client(that_pub, this_pri):
    print("채팅 서버 포트를 입력하세요: ")
    serve_port = int(input())
    server = threading.Thread(target=chat_server_thread
                              ,args=(serve_port,this_pri))
    server.start()

    print("접속할 포트를 입력하세요: ")
    dest_port = int(input())
    client = threading.Thread(target=chat_client_thread
                              ,args=(dest_port,that_pub))
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


if __name__ == '__main__':
    (this_pub, this_pri) = rsa.newkeys(128)
    print("Public: ", this_pub)
    print("Private: ", this_pri)

    that_pub = phase_get_key()
    phase_init_server_and_client(this_pri, that_pub)

