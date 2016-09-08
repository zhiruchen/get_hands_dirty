# -*- coding: utf-8 -*-

import socket

server_address = ('localhost', 10000)

def make_udp_server():

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("binding server on {}:{}".format(*server_address))

    sock.bind(server_address)

    while True:
        print("waiting for receiveing message...")
        data, address = sock.recvfrom(4096)

        print("received {} bytes from {}".format(len(data), address))
        print(data)

        if data:
            sent = sock.sendto(data, address)
            print("send {} bytes to {}".format(sent, address))

def make_udp_client():
    """make a echo udp client"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = b'the message to be sent to server'

    try:
        print("sending message to server")
        sent = sock.sendto()
    finally:
        pass
