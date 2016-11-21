#-*- coding:utf-8 -*-

"""
主机字节序和网络字节序的转换
"""

import socket


def convert_intefer():
    data = 1234
    print "Original: %s => Long host byte order: %s, Network byte order: %s" \
        % (data, socket.ntohl(data), socket.htonl(data))
    print "Original: %s => short host byte order: %s, network byte order: %s" \
        % (data, socket.ntohs(data), socket.htons(data))


if __name__ == '__main__':
    convert_intefer()
