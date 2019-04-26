def tcpConnect(HOST,PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    return s
    
def sendHeart(s):
    while True:
        s.sendall(b'hello??')
        time.sleep(20)
        data = s.recv(1024)
        if data == b'dis':
            break


class LongSocket:
    def __init__(self,HOST,PORT):
        # 开启 socket 链接
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((HOST, PORT))
        # 维护心跳??

    def sendHeart(self):
        # time interval
        pass

    def send(self,msg):
        self.s.sendall(bytes(msg,encoding='utf-8'))

    def recv(self):
        data = self.s.recv(1024)
        data.encode('utf-8')
        return data 

    def close(self):
        self.s.close()

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))

def send(HOST,PORT,msg):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(bytes(msg,'utf-8'))
        data = s.recv(1024)
        return data

def serve(HOST,PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                print(data.decode('utf-8'))

                if not data:
                    break
                conn.sendall(data)

def tcpServer(HOST,PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    return s


def serve(HOST,PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                print(data.decode('utf-8'))

                if not data:
                    break
                conn.sendall(data)

def serve_forever(conn):
    while True:
        data = conn.recv(1024)
        print(data.decode('utf-8'))
        if not data:
            break
        conn.sendall(data)
