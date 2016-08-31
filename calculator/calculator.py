# -*-coding: utf-8-*-

from operator import add, sub, mul, div, mod


class Calculator(object):
    """a simple calculator"""
    def __init__(self, exp_str):
        self.exp_str = exp_str

    def eval(self):
        """evaluate the value of exp_str
        (1 + 2) -> 3
        (1+(2*3)) -> 7
        ((2+(3*(5 - 1) / (8 / 2))) % 2) -> 0
        """
        suffix_exp = self.infix_to_suffix()
        return self.eval_suffix(suffix_exp)

    def infix_to_suffix(self):
        """中缀表达式转后缀表达式"""
        exp = self.exp_str.strip().replace(' ', '')
        digit_stack = []
        operator_stack = []
        for op in exp:
            if op.isdigit():  # 字符是数字
                digit_stack.append(op)
            elif self.is_operator(op):  # 是操作符
                operator_stack.append(op)
            elif op == ')':
                second_num = digit_stack.pop()
                first_num = digit_stack.pop()
                operator = operator_stack.pop()
                sub_suffix_str = ''.join(['(', operator, first_num, second_num, ')'])
                digit_stack.append(sub_suffix_str)
            elif op == '(':
                pass
            else:
                print "非法字符!"
                return

        return ''.join(digit_stack)

    def is_operator(self, op):
        return op in ['+', '-', '*', '/', '%']

    def eval_suffix(self, suffix_exp):
        """由后缀表达式求值"""
        val_stack = []
        op_stack = []
        for v in suffix_exp:
            if v.isdigit():
                val_stack.append(int(v))
            elif v == ')':
                vals = val_stack.pop(), val_stack.pop()
                val_stack.append(self.calcu_num(op_stack.pop(), *list(reversed(vals))))
            elif v != '(':
                op_stack.append(v)

        return val_stack.pop()

    def calcu_num(self, operator, *operands):
        if operator == '+':
            return add(*operands)
        elif operator == '-':
            return sub(*operands)
        elif operator == '*':
            return mul(*operands)
        elif operator == '/':
            dividend, divisor = operands
            if divisor == 0:
                raise ValueError('divisor is zero!')
            return float(div(float(dividend), divisor))
        elif operator == '%':
            return mod(*operands)
        else:
            raise ValueError('unknow operator!')
