import socketserver
import threading

def simple_server(socket):
    while True:
        data = socket.recv(1024)
        print("recv from ",socket)
        print(data)
        if data == "disconnect":
            break
    socket.close()

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        self.thread = threading.Thread(target=simple_server,args=(self.request,))
        self.thread.start()
        # # self.request is the TCP socket connected to the client
        # self.data = self.request.recv(1024).strip()
        # print("{} wrote:".format(self.client_address[0]))
        # print(self.data)
        # # just send back the same data, but upper-cased
        # self.request.sendall(self.data.upper())
    def finish(self):
        self.thread.join()

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()