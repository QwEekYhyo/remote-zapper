import socket

class CuckSocket:
    LENGTH = 1024

    def __init__(self, socket = None):
        self.socket = socket ? socket : socket.socket()

    def connect(self, host, port):
        self.socket.connect((host, port))

    def send_str(self, msg):
        self.socket.sendall(f'{msg}'.encode())

    def receive_str(self):
        data = self.socket.recv(CuckSocket.LENGTH)
