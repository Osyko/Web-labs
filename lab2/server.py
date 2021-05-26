from socket import socket, AF_INET, SOCK_STREAM, SO_RCVBUF, SOL_SOCKET
from select import select
import json


#const
HOST = 'localhost'
PORT = 8020
CODDING = 'utf-8'
CLIENT_QUEUE_LEN = 15


#function 
def square_area(N):
    N = pow(int(N), 2)
    return N


def httpPost(N:int):
    message = json.dumps({'div': N})
    content_length = len(str(message))
    http_post = f'HTTP/1.1 200 OK\n' \
               f'Host: {HOST}\n' \
               f'Port: {PORT}\n' \
               f'Content-Type: text/html\n' \
               f'Content-Length: {content_length}\n' \
               f'\n' \
               f'{message}' \
               f'\n'
    return http_post


def parserHttpGet(http:str):
    get, message = http.split('\n\n')
    message = json.loads(message)
    get = get.split('\n')
    line_one = get[0].split()
    get_dict = {'Method': line_one[0],
                'Uri': line_one[1],
                'Protocol': line_one[2].split('/')[0],
                'Protocol-Version': line_one[2].split('/')[1]}
    for line in range(1, len(get)):
        key, value = get[line].split(': ')
        get_dict[key] = value

    return get_dict, message


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

#main function
def main():

    #create server socket
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(CLIENT_QUEUE_LEN)

    #lists for sockets
    read_list = [server]
    write_list = []
    except_list = [server]

    messages = {}

    print("Server is running")
    while True:
        read, write, exception = select(read_list, write_list, except_list)

        for r in read:
            if r is server:
                client, _ = server.accept()
                read_list.append(client)
            else:
                data = read_from_socket(r)
                http, message = parserHttpGet(data.decode(CODDING))
                print(f"message: {message}\npars Http: {http}")
                message = square_area(message['N'])
                data = httpPost(message)
                messages[r] = data
                write_list.append(read_list.pop(1))

        for w in write:
            data = messages[w]
            w.send(data.encode(CODDING))
            write_list.pop(0).close()

        for e in exception:
            if e is server:
                break
            else:
                except_list.pop(1).close()


if __name__ == '__main__':
    main()