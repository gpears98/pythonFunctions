import socket

class TCPClient:
    def __init__(self, host, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port

    def connect(self):
        self.client.connect((self.host, self.port))
    
    def send(self):
        data = f"GET / HTTP/1.1\r\nHost:{self.host}\r\n\r\n"
        self.client.send(data.encode())

    def recv(self):
        return self.client.recv(4096).decode()

    def close(self):
        self.client.close()
