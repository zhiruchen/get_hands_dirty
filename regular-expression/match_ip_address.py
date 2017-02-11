# encoding: utf-8

import re

"""
正则表达式匹配ip地址
"""

PATTERN = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'


def match_ips():
    with open('ip_address.txt', 'r') as f:
        for line in f:
            result = re.match(PATTERN, line)
            if result:
                print result.group(0)
