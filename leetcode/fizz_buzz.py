# encoding: utf-8

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ll = []
        for x in range(1, n+1):
            if x % (3 * 5) == 0:
                ll.append("FizzBuzz")
            elif x % 3 == 0:
                ll.append("Fizz")
            elif x % 5 == 0:
                ll.append("Buzz")
            else:
                ll.append(str(x))

        return ll