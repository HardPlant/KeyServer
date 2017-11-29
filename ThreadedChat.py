from chat_client import ChatClient
from chat_server import ChatServer
from key_client import KeyClient
import threading


def chat_server_thread(port):
    chat_server = ChatServer(port)
    chat_server.serve()


def chat_client_thread(port):
    chat_client = ChatClient(port)
    while True:
        print('Send Message> ')
        msg = input()
        chat_client.send_message(msg)


if __name__ == '__main__':
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

