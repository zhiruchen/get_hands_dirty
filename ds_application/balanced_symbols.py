# -*- encoding: utf-8 -*-

"""
符号匹配
"""

from datastructure.stack import Stack

OPEN_CHARS = "([{"
CLOSE_CHARS = ")]}"


def match(open_char, close_char):
    """open_char, close_char是否匹配"""
    if open_char in OPEN_CHARS and close_char in CLOSE_CHARS:
        return OPEN_CHARS.index(open_char) == CLOSE_CHARS.index(close_char)

    return False


def symbol_match(symbol_str):
    balanced = True
    stack = Stack()

    for s in symbol_str:
        if s in OPEN_CHARS:
            stack.push(s)
        else:
            if stack.is_empty():
                balanced = False
                break
            else:
                top_val = stack.pop()
                if not match(top_val, s):
                    balanced = False
                    break

    return balanced and stack.is_empty()


def test_symbol_match():
    assert symbol_match("([{}])") is True
    assert symbol_match("((){}[})") is False

    print symbol_match("([{}])")
    print symbol_match("((){}[})")


if __name__ == '__main__':
    test_symbol_match()
