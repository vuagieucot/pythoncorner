import socket
import pickle

class Network:
    def __init__(self, server='192.168.0.23', port=5555):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server
        self.port = port
        self.addr = (self.server, self.port)
        self.data = self.connect()

    def get_data(self):
        return self.data

    def connect(self):
        try:
            self.s.connect(self.addr)
            return self.s.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.s.send(str.encode(data))
            return pickle.loads(self.s.recv(2048))
        except socket.error as e:
            print(e)