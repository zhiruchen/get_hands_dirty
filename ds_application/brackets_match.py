# -*- encoding: utf-8 -*-

"""
栈应用: 括号匹配
"""
from datastructure.stack import Stack


def brackets_match(bracket_str):
    """括号匹配"""
    balanced = True
    stack = Stack()

    for s in bracket_str:
        if s == '(':
            stack.push(s)
        else:
            if stack.is_empty():
                balanced = False
                break
            else:
                stack.pop()

    return balanced and stack.is_empty()


def test_brackets_match():
    assert brackets_match('((()))') is True, 'match test success'
    assert brackets_match('(((()))') is False, 'unmatch test success'


if __name__ == '__main__':
    test_brackets_match()
