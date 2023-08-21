import socket
from sound import Audio

def handle_signal(num, audio):
    if num == 1:
        audio.increase_volume()
        print("Volume has been increased")
    elif num == -1:
        audio.reduce_volume()
        print("Volume has been decreased")
    elif num == 0:
        audio.reset()
    else:
        print(f'Received {num}')

HOST = ''
PORT = 50007

audio = Audio()

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
        handle_signal(decoded, audio)
    except ValueError:
        print("Received non-integer data")
