import socket, socketserver
from sys import argv, exit, stderr
import os

PORTNO = 8042

BUFSIZE = 4096

class FileTCPServer(socketserver.BaseRequestHandler):

    def handle(self):
        # According to the protocol, this is the name of the file to be accessed
        self.data = self.request.recv(1024).strip()

        print("Request for {}".format(self.data))

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

if __name__ == "__main__":
    HOST, PORT = "localhost", 8042

    with socketserver.TCPServer((HOST, PORT), FileTCPServer) as server:

        server.serve_forever()
