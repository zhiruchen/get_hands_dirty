# encoding: utf-8
"""a tiny interprter
    http://qingyunha.github.io/taotao/
"""


class Interprter(object):
    def __init__(self):
        self.stack = []

    def load_value(self, number):
        self.stack.append(number)

    def print_answer(self):
        answer = self.stack.pop()
        print answer

    def add_two_value(self):
        num1 = self.stack.pop()
        num2 = self.stack.pop()
        self.stack.append(num1 + num2)


    def run_code(self, code):
        instrucs = code["instructions"]
        numbers = code["numbers"]

        for exp in instrucs:
            ins, arg = exp
            if ins == "LOAD_VALUE":
                self.load_value(numbers[arg])
            elif ins == "ADD_TWO_VALUES":
                self.add_two_value()
            elif ins == "PRINT_ANSWER":
                self.print_answer()


if __name__ == '__main__':
    interpreter = Interprter()
    interpreter.run_code({
        "instructions":[
            ("LOAD_VALUE", 0),
            ("LOAD_VALUE", 1),
            ("ADD_TWO_VALUES", None),
            ("PRINT_ANSWER", None)
        ],
        "numbers": [7, 5]
    })
    