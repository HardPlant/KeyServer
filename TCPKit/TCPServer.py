import socket
import threading


class TCPServer:
    def __init__(self, port, handler):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port
        self.handler = handler

    def serve_forever(self):
        self.socket.bind(("", self.port))
        self.socket.listen(5)
        while True:
            client_socket, address = self.socket.accept()
            t = threading.Thread(target=self.routine
                                 , args=(client_socket, self.handler))
            t.start()

    def serve_once(self):
        self.socket.bind(("", self.port))
        self.socket.listen(5)
        result = []
        client_socket, address = self.socket.accept()
        t = threading.Thread(target=self.routine_result
                             , args=(client_socket, self.handler, result))
        t.start()
        t.join()
        return result[0]

    def routine(self, socket, handler):
        try:
            handler(socket)
        finally:
            socket.close()

    def handler(self, socket):
        pass

    def routine_result(self, socket, handler, result):
        try:
            result.append(handler(socket))
        finally:
            socket.close()


