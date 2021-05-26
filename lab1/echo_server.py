'''import sys
import socket
import json
from threading import Thread

def square_area(n):
    n = pow(int(n), 2)
    return n

def server(c: socket, client_address):
    print(sys.stderr, 'waiting for a connection')
    size = c.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    data = c.recv(size)
    data = json.loads(data.decode("utf-8"))
    print(f'{client_address} >> Area = {data["request"]} cm')
    print(sys.stderr, 'received "%s"' % data)
    print(sys.stderr, 'sending data back to the client')
    data = json.dumps({"result": square_area(data['request'])}).encode("utf-8")
    c.sendall(data)
    c.close()

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 1025)
    sock.bind(server_address)
    sock.listen(15)
    while True:
        connection, client_address = sock.accept()
        client = Thread(target=server, args=(connection,))
        print(sys.stderr, 'connection from', client_address)
        client.start()

if __name__ == '__main__':
    main()
'''

from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_RCVBUF
from threading import Thread
import json

# const
HOST = "localhost"
PORT = 1025
CODING = "utf-8"


def square_area(n):
    n = pow(int(n), 2)
    return n


def server(s: socket, address):
    print(f'Got connection from {address}')
    size = s.getsockopt(SOL_SOCKET, SO_RCVBUF)
    # read message
    data = s.recv(size)
    data = json.loads(data.decode(CODING)) #->dict
    print(f'{address} >> side = {data["request"]} cm')
    # message encoding (json)
    data = json.dumps({"message": f"area = {square_area(data['request'])} cm^2\n"}).encode(CODING)
    # sending a message to client
    s.send(data)
    s.close()


# main function
def main():
    # create socket
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(15)
    print("Server started!")
    print("Waiting for clients...")
    while True:
        client_sock, address = sock.accept()
        client = Thread(target=server, args=(client_sock, address,))
        client.start()

if __name__ == '__main__':
    main()
