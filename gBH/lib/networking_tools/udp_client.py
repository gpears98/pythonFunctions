import socket

class UDPClient:
    def __init__(self, host, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host = host
        self.port = port
        
    def send(self):
        self.client.sendto(b"AAABBBCCC", (self.host, self.port))
        
    def recv(self):
        data, addr = self.client.recvfrom(4096)
        return data.decode(), addr

    def close(self):
        self.client.close()
