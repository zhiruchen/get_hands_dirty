# -*- coding:utf-8 -*-

"""
Host Name TimesLight
IP Address: 192.168.56.1
"""

import socket


def print_machine_info():
    host_name = socket.gethostname()
    print "Host Name %s" % host_name

    ip_address = socket.gethostbyname(host_name)
    print "IP Address: %s" % ip_address


if __name__ == '__main__':
    print_machine_info()



