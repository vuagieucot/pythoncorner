import socket
from _thread import start_new_thread
from samples.player import Player
import pickle

# hostname = socket.gethostname()
# server = socket.gethostbyname(hostname)
server = '192.168.0.70'
port = 5555

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    print(e)

s.listen(3)
print('Waiting for a connection...')

players = [Player(0,0,50,50,(255,0,255)), Player(100,100,50,50,(0,255,255)), Player(200,200,50,50,(255,255,0))]

def threaded_client(conn, curP):
    conn.send(pickle.dumps(players[curP]))
    reply = ''
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[curP] = data
            if not data:
                print('Disconnected')
                break
            else:
                if curP == 1:
                    reply = (players[0], players[2])
                elif curP == 2:
                    reply = players[0], players[1]
                else:
                    reply = players[1], players[2]
                print('Received: {}'.format(data))
                print('Sending: {}'.format(reply))
            conn.sendall(pickle.dumps(reply))
        except:
            print(reply)
            break

    print('Lost connection')
    conn.close()

curP = 0
while True:
    if curP > 3:
        raise ValueError('Number of Player exceeded the limit.')
    conn, addr = s.accept()
    print('Connected to: {}'.format(addr))

    start_new_thread(threaded_client, (conn, curP))
    curP += 1