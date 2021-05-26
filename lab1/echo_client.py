'''import socket
import sys
import json
from threading import Thread
import random

def client(n, side):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 1025)
    print(sys.stderr, 'connecting to %s port %s' % server_address, 'client # ', n)
    sock.connect(server_address)
    print(sys.stderr, 'sending "%s"' % side)
    sock.sendall(json.dumps({"request": side}).encode("utf-8"))
    size = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    data = json.loads(sock.recv(size).decode("utf-8"))
    print(sys.stderr, 'received "%s"' % data)

def main():
    for i in range(15):
        side = random.randint(1, 20)
        client_1 = Thread(target=client, args=(i+1, side,))
        client_1.start()
        client_1.join()

    print("Finish")


if __name__ == '__main__':
    main()
'''

from threading import Thread
from socket import socket, SOL_SOCKET, SO_RCVBUF
import json
from random import randint


# const
HOST = "localhost"
PORT = 1025
CODING = "utf-8"


def client(n, side):
    # create socket
    sock = socket()
    print(f"Connecting to {HOST} {PORT}, client #{n}")
    sock.connect((HOST, PORT))
    # create message
    msg = json.dumps({"request": side}).encode(CODING)
    # sending a message to server
    sock.send(msg)
    # decoding message from json
    size = sock.getsockopt(SOL_SOCKET, SO_RCVBUF)
    data = json.loads(sock.recv(size).decode())
    print(f"SERVER >> {sock.getsockname()[1]}: {data['message']}")


def main():
    # creating threads
    for i in range(15):
        side = randint(1, 20)
        client_1 = Thread(target=client, args=(i+1, side))
        client_1.start()
        client_1.join() #waiting when thread ends up

    print("Finish")


if __name__ == '__main__':
    main()


