# -*- coding:utf-8 -*-

"""
ip 地址转换
"""
import socket
from binascii import hexlify


def convert_ip4_address():
    for ip in ['127.0.0.1', '192.168.0.1']:
        packed_address = socket.inet_aton(ip)
        unpacked_address = socket.inet_ntoa(packed_address)
        print "ip_address: %s => packed_address: %s, unpacked: %s" % \
              (ip, hexlify(packed_address), unpacked_address)


if __name__ == '__main__':
    convert_ip4_address()
