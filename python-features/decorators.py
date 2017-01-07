# -*- encoding: utf-8 -*-

"""
装饰器
"""

from functools import wraps

# ---------------函数装饰器------------
def func_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print "calling %s" % func.__name__
        result = func(*args, **kwargs)
        print "end calling %s" % func.__name__
        return result

    return wrapper


# ----------------类装饰器----------------
class Decorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print "before calling %s" % self.func.__name__
        result = self.func(*args, **kwargs)
        print "after calling %s" % self.func.__name__
        return result


@func_decorator
def my_func1(x, y):
    """
    my_func1
    result <=> func_decorator(my_func1)(x, y)
    """
    return x + y


@Decorator
def my_func2(a, b):
    """
    result <=> Decorator(my_func2)(a, b)
    """
    return a ** b


"""
calling my_func1
end calling my_func1
7
before calling my_func2
after calling my_func2
1024
"""

if __name__ == '__main__':
    print my_func1(3, 4)
    print my_func2(2, 10)
