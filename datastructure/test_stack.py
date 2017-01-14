# -*- encoding: utf-8 -*-

import unittest

from stack import Stack


class TestStack(unittest.TestCase):
    """docstring for TestStack."""
    def setUp(self):
        pass

    def testpush(self):
        stack = Stack()
        self.assertEqual(len(stack), 0)
        stack.push("A")
        stack.push("B")
        stack.push("C")
        stack.push("D")
        self.assertEqual(len(stack), 4)

    def testpop(self):
        stack = Stack()
        self.assertEqual(stack.pop(), None)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(6)
        self.assertEqual(stack.pop(), 6)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), None)

    def testpeek(self):
        stack = Stack()
        self.assertEqual(stack.peek(), None)

        stack.push(1)
        stack.push(100)
        self.assertEqual(stack.peek(), 100)


if __name__ == '__main__':
    unittest.main()
