from socket import socket, SOL_SOCKET, SO_RCVBUF
from threading import Thread
from random import randint
import json


HOST = 'localhost'
PORT = 8020
CODDING = 'utf-8'
CLIENT_QUEUE_LEN = 15


def HttpGet(N: int) -> str:
    message = json.dumps({'N': N})
    context_length = len(str(message))
    http_get = f'GET /BS-91/Osyko HTTP/1.1\n' \
               f'Host: {HOST}\n' \
               f'Port: {PORT}\n' \
               f'Content-Type: text/html\n' \
               f'Content-Length: {context_length}\n' \
               f'\n' \
               f'{message}' \
               f'\n'
    return http_get


def parserHttpPost(http: str):
    post, message = http.split('\n\n')
    message = json.loads(message)
    post = post.split('\n')
    lineOne = post[0].split()
    post_dict = {'Method': 'POST',
                 'Protocol': lineOne[0].split('/')[0],
                 'Protocol-Version': lineOne[0].split('/')[1],
                 'Status': lineOne[1],
                 'Status-Description': lineOne[2]}
    for line in range(1, len(post)):
        key, value = post[line].split(': ')
        post_dict[key] = value

    return post_dict, message


def read_from_socket(s:socket):
    data = b''
    buff_size = s.getsockopt(SOL_SOCKET, SO_RCVBUF)
    while True:
        chunk = s.recv(buff_size)
        if chunk:
            data += chunk
        if chunk==b'' or chunk.decode()[-1] == '\n':
            break
    return data


def client_request(N: int, thread_num: int):
    client = socket()
    client.connect((HOST,PORT))
    data = HttpGet(N)
    client.send(data.encode())

    data = read_from_socket(client)

    http, message = parserHttpPost(data.decode(CODDING))
    print(f"thread: {thread_num} -> Area with {N} sm side = {message['div']} sm")
    print('pars Http: ', http)
    client.close()

def main():
    print("Start")

    numbers = [randint(13, 1013) for i in range(CLIENT_QUEUE_LEN)]
    thread_list = []

    for i in range(CLIENT_QUEUE_LEN):
        client = Thread(target=client_request, args=(numbers[i], i+1))
        thread_list.append(client)
        client.start()

    for thread in thread_list:
        thread.join()

    print("Finish")


if __name__ == '__main__':
    main()