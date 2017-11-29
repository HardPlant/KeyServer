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

