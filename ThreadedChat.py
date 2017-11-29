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
    print("[Server] Private: ", pri)
    exchange_server = ExchangeServer(port, pri)
    sym_key = exchange_server.serve()
    print("[Server] sym_key: ", sym_key)
    return

    chat_server = ChatServer(port, sym_key)
    chat_server.serve()

def chat_client_thread(port, pub):
    print("[Client] Public: ", pub)
    exchange_client = ExchangeClient(port, pub)
    sym_key = chat_client_gen_sym_key()
    print("[Client] sym_key: ", sym_key)
    exchange_client.send_message(sym_key)
    return

    chat_client = ChatClient(port, sym_key)
    while True:
        print('Send Message> ')
        msg = input()
        chat_client.send_message(msg)

def phase_init_server_and_client(this_pri, that_pub):
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
        that_pubkey_n, that_pubkey_e = key_client.get_pubkey(that_id)
        print("n ", that_pubkey_n, 'e', that_pubkey_e)
        if that_pubkey_n != 0:
            break
        print("잘못된 id입니다.")

    return rsa.PublicKey(that_pubkey_n, that_pubkey_e)

def phase_generate_key():
    this_pub = 0
    this_pri = 0
    print("1 or 2")
    id = input()

    if(id == '1'):
        this_pub = rsa.PublicKey(202137387733458537301164105994247647661, 65537)
        this_pri = rsa.PrivateKey(202137387733458537301164105994247647661, 65537,
                                  56430804674784585731965153685654373665, 181785849768822681379, 1111953367055339759)
    if(id == '2'):
        this_pub = rsa.PublicKey(228824876101654018166397806380867770343, 65537)
        this_pri = rsa.PrivateKey(228824876101654018166397806380867770343, 65537,
                                  133415129479840421135250387360768543713, 213929244404772581873, 1069628777207746391)
    # (this_pub, this_pri) = rsa.newkeys(128)
    print("Public: ", this_pub)
    print("Private: ", this_pri)

    return (this_pub, this_pri)

if __name__ == '__main__':
    this_pub, this_pri = phase_generate_key()
    that_pub = phase_get_key()
    print(that_pub)
    phase_init_server_and_client(this_pri, that_pub)

