import TCPKit.TCPServer as TCPServer

def handler(sock):
    msg = sock.recv(1024)
    sock.send(msg)

if __name__ == '__main__':
    server = TCPServer.TCPServer(12345,handler)
    server.serve_forever()
