# -*- encoding: utf-8 -*-

"""
10进制转2进制
"""

from datastructure.stack import Stack


def convert_to_binary(number):
    s = Stack()

    while number:
        s.push(number % 2)
        number /= 2

    bin_digits = []
    while not s.is_empty():
        bin_digits.append(str(s.pop()))

    return ''.join(bin_digits)


def test_convert_to_binary():
    assert convert_to_binary(123) == '1111011'
    assert convert_to_binary(100) == '1100100'
    assert convert_to_binary(1) == '1'
    assert convert_to_binary(0) == ''

if __name__ == '__main__':
    test_convert_to_binary()
