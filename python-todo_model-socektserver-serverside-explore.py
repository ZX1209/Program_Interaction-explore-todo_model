import socketserver

import argparse

# setup
parser = argparse.ArgumentParser()


parser.add_argument("action", type=str,
                    choices=[
                        'todo',
                        'done',
                        'show',
                        'update',
                        'del',
                        'create'
                    ])
parser.add_argument("object", type=str,nargs='+')


def todo_handle(args):
    try:
        # args parser
        args = parser.parse_args(args)

        # handle
        if args.action:
            if args.action == "todo":
                print("todo", args.object)
            elif args.action == "done":
                print("done", args.object)
            elif args.action == "show":
                print("show", args.object)
            elif args.action == "update":
                if args.to:
                    print("update", args.object,'to',args.to)
            else:
                print('not difined')
    except:
        print("error ??")



class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024)
        self.data = self.data.decode('utf-8')
        self.data = self.data.split()
        print("{} wrote:".format(sefl.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        todo_handle(self.data)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()