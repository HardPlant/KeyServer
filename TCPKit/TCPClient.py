import socket
import threading

class TCPClient:
    def __init__(self, dest, port, handler):
        self.dest = dest
        self.port = port
        self.handler = handler

    def run(self, args=None):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.dest, self.port))
        t = threading.Thread(target=self.routine
                             , args=(sock, self.handler, args))
        t.start()

    def routine(self, socket, handler, args):
        try:
            handler(socket, args)
        finally:
            socket.close()

    def handler(self, socket, args=None):
        pass

