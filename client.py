import socket

def send_signal(host, port, num):
    s = socket.socket()
    s.connect((host, port))
    s.sendall(f'{num}'.encode())
    s.close()

HOST = "localhost"
PORT = 50007

working = True
while working:
    data = input("Enter a number : ")
    if data == 69:
        working = False
    else:
        send_signal(HOST, PORT, data)
