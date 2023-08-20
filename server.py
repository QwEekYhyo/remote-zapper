import socket

def handle_signal(num):
    if num == 1:
        print("Volume has been increased")
    elif num == -1:
        print("Volume has been decreased")
    else:
        print(f'Received {num}')

HOST = ''
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

while True:
    conn, addr = s.accept()
    print("Connected by", addr)
    data = conn.recv(1024)
    decoded = None
    try:
        decoded = int(data)
        handle_signal(decoded)
    except ValueError:
        print("Received non-integer data")
