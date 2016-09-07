# -*- coding: utf-8 -*-

import socket
import sys


def make_server():
    # 创建tcp/ip连接
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind the socket to the 10000 port
    sock.bind(('localhost', 10000))

    #
    print("listening in {}:{}".format(*('localhost', 10000)))
    sock.listen(1)

    #
    while True:
        connection, client_address = sock.accept()

        try:
            print("connection from ", client_address)

            while True:
                data = connection.recv(16)
                print("recived {!r}".format(data))

                if data:
                    print("sending back to client")
                    connection.sendall(data)
                else:
                    print("no data ", client_address)
                    break
        finally:
            connection.close()


def make_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 10000)

    print("connect to {}:{}".format(*server_address))
    sock.connect(server_address)

    try:
        message = b'this is the message'
        sock.sendall(message)

        received_count = 0
        expect_count = len(message)
        while received_count < expect_count:
            data = sock.recv(16)
            received_count += len(data)
            print("received {!r}".format(data))

    finally:
        print("closing connection")
        sock.close()


if __name__ == '__main__':
    make_server()
    # make_client()