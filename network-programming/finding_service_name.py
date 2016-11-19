# -*- coding:utf-8 -*-

"""
找到网络服务的名字
"""

import socket

def find_service_name():
    protocol_name = 'tcp'
    for port in [80, 25]:
        print "Port: %s => service: %s" % (port, socket.getservbyport(port, protocol_name))

    print "Port: %s => service: %s" % (53, socket.getservbyport(53, 'udp'))


if __name__ == '__main__':
    find_service_name()

# Port: 80 => service: http
# Port: 25 => service: smtp
# Port: 53 => service: domain
