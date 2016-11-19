# -*- coding:utf-8 -*-

"""
获取远程设备的IP地址
"""
import socket


def get_remote_machine_info():
    remote_host = 'zeblog.farbox.com'
    try:
        print "remote IP address: %s" % socket.gethostbyname(remote_host)
    except socket.error, errmsg:
        print "%s: %s" % (remote_host, errmsg)


if __name__ == '__main__':
    get_remote_machine_info()
