import socket
from sys import argv, exit, stderr

BUFSIZE = 4096

PORTNO = 8042

if __name__ == "__main__":

    n = len(argv)
    if n != 3:
        print("usage: python3 client.py <server> <file>", file = stderr)
        exit()

    __, server_address, file_path = argv

    HOST, PORT = server_address, PORTNO

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(bytes(file_path, "UTF-8"))
        sock.shutdown(socket.SHUT_WR)

        response_type = sock.recv(7)
        
        if response_type == "FAILURE":
            print("Unable to access file {} on {}".format(file_path,
                server_address))

        else:
            # Assumption: Client only asks for text files
            while True:
                data = str(sock.recv(BUFSIZE), "UTF-8")
                print(data, end = "")
                if len(data) == 0:
                    break
