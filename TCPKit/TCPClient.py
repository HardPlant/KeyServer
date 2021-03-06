import socket
import threading


class TCPClient:
    def __init__(self, dest, port, handler):
        self.dest = dest
        self.port = port
        self.handler = handler

    def run(self, *args): # args[1] must be result
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.dest, self.port))
        t = threading.Thread(target=self.routine
                             , args=(sock, self.handler, *args))
        t.start()
        t.join()

    def routine(self, socket, handler, *args): # args[1] = result queue
        if args == None :
            result = []
        else:
            result = args[1]
        try:
            result.append(handler(socket, *args))
        finally:
            socket.close()

    def handler(self, socket, *args):
        pass

