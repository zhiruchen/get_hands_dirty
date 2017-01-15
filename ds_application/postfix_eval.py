# -*-encoding: utf-8 -*-

"""
后缀表达式求值
从左向右扫描表达式：遇到操作数入栈；
遇到操作符，弹出最近的两个操作数进行运算，然后将结果入栈；
当最后一个操作符被处理后u，栈中只剩一个值，就是后缀表达式的值
"""
from datastructure.stack import Stack


def do_math(operator, operand1, operand2):
    if not (operator and operand1 and operand2):
        raise ValueError("invalid operator")

    if operator == '+':
        return int(operand1) + int(operand2)
    elif operator == '-':
        return int(operand1) - int(operand2)
    elif operator == '*':
        return int(operand1) * int(operand2)
    elif operator == '/':
        return int(operand1) / int(operand2)
    else:
        raise ValueError("invalid operator")


def postfix_eval(postfix):
    """后缀表达式求值"""
    if not postfix:
        return

    operand_stack = Stack()
    for symbol in postfix:
        if symbol.isdigit():
            operand_stack.push(symbol)
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(symbol, operand1, operand2)
            operand_stack.push(result)

    return operand_stack.pop()  # 返回最终的计算结果


def test_postfix_eval():
    from infix_to_postfix import infix_to_postfix
    assert postfix_eval(infix_to_postfix("(1+2)*3-(4-1)*(5+6)")) == -24
    assert postfix_eval(infix_to_postfix("(1+2)*(3+4)")) == 21
    assert postfix_eval(infix_to_postfix("(1+2)*3")) == 9

    print postfix_eval(infix_to_postfix("(1+2)*3-(4-1)*(5+6)"))
    print postfix_eval(infix_to_postfix("(1+2)*(3+4)"))
    print postfix_eval(infix_to_postfix("(1+2)*3"))
