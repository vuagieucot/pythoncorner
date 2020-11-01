import socket
from _thread import *

hostname = socket.gethostname()
server = socket.gethostbyname(hostname)
# server = '192.168.0.70'
port = 5555

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    print(e)

s.listen(2)
print('Waiting for a connection...')

def threaded_client(conn):
    reply = ''
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')
            if not data:
                print('Disconnected')
                break
            else:
                print('Received: {}'.format(reply))
                print('Sending: {}'.format(reply))
            conn.sendall(str.encode(reply))
        except:
            print(reply)
            break

while True:
    conn, addr = s.accept()
    print('Connected to: {}'.format(addr))

    start_new_thread(threaded_client, (conn, ))