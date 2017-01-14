# -*- encoding: utf-8 -*-

"""
中缀转后缀
"""

from datastructure.stack import Stack


OPERATOR_PRECEDENCE = {
    "(": 1,
    "+": 2,
    "-": 2,
    "*": 3,
    "/": 3
}


def is_operand(token):
    """是否是操作数"""
    return token.isdigit()


def is_operator(token):
    return token in ['+', '-', '*', '/']


def higher_precedence(first_op, second_op):
    return OPERATOR_PRECEDENCE[first_op] >= OPERATOR_PRECEDENCE[second_op]


def infix_to_postfix(infix):
    """
    中缀转后缀
    :param infix:中缀表达式
    :return: 后缀表达式
    """
    opstack = Stack()  # 操作符栈
    result = []

    for token in infix:
        if is_operand(token):  # 操作数
            result.append(token)
        elif token == '(':     # 遇到左括号，入栈
            opstack.push(token)
        elif token == ')':     # 遇到右括号，弹栈并将值放至result列表末尾, 直到遇到左括号
            _token = opstack.pop()
            while _token and _token != '(':
                result.append(_token)
                _token = opstack.pop()

        else:                   # 遇到操作符，压栈，但是如果在栈中有比当前操作符优先级高的任何操作符要先弹出
            while not opstack.is_empty():
                top_token = opstack.peek()
                if higher_precedence(top_token, token):
                    result.append(opstack.pop())
                else:
                    break
            opstack.push(token)

    while not opstack.is_empty():
        result.append(opstack.pop())

    return ''.join(result)


def test_infix_to_postfix():
    assert infix_to_postfix("(1+2)*3") == "12+3*"
    assert infix_to_postfix("(1+2)*(3+4)") == "12+34+*"
    assert infix_to_postfix("(1+2)*3-(4-1)*(5+6)") == "12+3*41-56+*-"
    print infix_to_postfix("(1+2)*3")
    print infix_to_postfix("(1+2)*(3+4)")
    print infix_to_postfix("(1+2)*3-(4-1)*(5+6)")


if __name__ == '__main__':
    test_infix_to_postfix()
