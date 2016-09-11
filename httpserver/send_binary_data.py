# -*- coding: utf-8 -*-

import binascii
import socket
import struct


def make_server():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 10000)
    sock.bind(server_address)
    sock.listen(1)

    unpacker = struct.Struct('I 2s f')

    while True:
        print("waiting for a connection")
        connection, address = sock.accept()

        try:
            data = connection.recv(unpacker.size)
            print("received {!r}".format(binascii.hexlify(data)))

            unpack_data = unpacker.unpack(data)
            print("unpackered {}",format(unpack_data))

        finally:
            connection.close()


def make_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 10000)

    sock.connect(server_address)

    values = (1, b'ab', 2.7)
    packer = struct.Struct('I 2s f')
    pack_data = packer.pack(*values)

    try:
        print("sending {!r}".format(binascii.hexlify(pack_data)))
        sock.sendall(pack_data)

    finally:
        sock.close()


if __name__ == '__main__':
    make_server()

# waiting for a connection
# received b'0100000061620000cdcc2c40'
# unpackered {} (1, b'ab', 2.700000047683716)
# waiting for a connection
