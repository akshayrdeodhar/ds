import socket, socketserver
from sys import argv, exit, stderr
import os

PORTNO = int(os.environ['SERVICE_PORT'])

BUFSIZE = 4096

class FileTCPServer(socketserver.BaseRequestHandler):

    def handle(self):

        print("Handling Request")

        # According to the protocol, this is the name of the file to be accessed
        self.data = self.request.recv(1024).strip()

        print("Request for {}, handled by {}, child of {}".format(self.data,
            os.getpid(), os.getppid()))

        if os.path.isfile(self.data):
            nature = "SUCCESS"
        else:
            nature = "FAILURE"

        self.request.send(bytes(nature, "UTF-8"))

        if nature == "SUCCESS":
            file_name = self.data
            with open(file_name, "r") as fp:
                while True:
                    data = fp.read(BUFSIZE)
                    self.request.send(bytes(data, "UTF-8"))
                    if len(data) < BUFSIZE:
                        break

        self.request.shutdown(socket.SHUT_RDWR)

# Server which forks and lets the child handle each client
class ForkingTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":

    HOST, PORT = "0.0.0.0", PORTNO

    print("Server PID: {}".format(os.getpid()))

    with ForkingTCPServer((HOST, PORT), FileTCPServer) as server:

        server.serve_forever()
