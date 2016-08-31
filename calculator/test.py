# -*-coding:utf-8 -*-

from calculator import Calculator


def test_infix_to_suffix():
    calcu = Calculator('((2+(((3*(5 - 1)) / (8 / 2))) % 2)')
    print calcu.infix_to_suffix()

    calcu = Calculator('(1 + 2)')
    print calcu.infix_to_suffix()

    calcu = Calculator('(1+(2*3))')
    print calcu.infix_to_suffix()


def test_eval():
    calcu = Calculator('(1 + 2)')
    print calcu.eval()

    calcu = Calculator('(1+(2*3))')
    print calcu.eval()

    calcu = Calculator('((2+(((3*(5 - 1)) / (8 / 2))) % 2)')
    print calcu.eval()


if __name__ == '__main__':
    test_infix_to_suffix()
    test_eval()
