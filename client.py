import socket

def send_signal(host, port, num):
    s = socket.socket()
    s.connect((host, port))
    s.sendall(f'{num}'.encode())
    s.close()

HOST = "192.168.1.4"
PORT = 50007

working = True
while working:
    data = input("Enter a number : ")
    if data == "stop":
        working = False
    else:
        send_signal(HOST, PORT, data)
