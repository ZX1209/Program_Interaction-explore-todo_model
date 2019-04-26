import socket

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        cmdline = input('cmd:')
        s.sendall(bytes(cmdline,encoding='utf-8'))
        data = s.recv(1024)
        print('Received', repr(data))