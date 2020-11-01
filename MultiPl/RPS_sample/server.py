import socket
import pickle

from _thread import start_new_thread
try:
    from RPS_sample.rps import RPS
except:
    from rps import RPS

server = '192.168.0.23'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen()
print('Waiting for a connection...')

connected = set()
games = {}
idCount = 0

def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ''
    while True:
        try:
            data = conn.recv(4096).decode()

            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == 'reset':
                        game.resetMove()
                    elif data != 'get':
                        game.play(p, data)
                    reply = game
                    conn.sendall(pickle.dumps(reply))
            else:
                break
        except:
            break

    print('Lost connection')
    try:
        del games[gameId]
        print('Closing game {}'.format(gameId))
    except:
        pass
    idCount -= 1
    conn.close()

while True:
    conn, addr = s.accept()
    print('Connected to: {}'.format(addr))
    idCount += 1
    p=0
    gameId = (idCount -1)//2
    print(gameId)
    if idCount % 2 == 1:
        games[gameId] = RPS(gameId)
        print('Created a new game...')
    else:
        games[gameId].ready = True
        p = 1

    start_new_thread(threaded_client, (conn, p, gameId))