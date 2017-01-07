# -*- encoding: utf-8 -*-

"""
描述符
实现了__get__, __set__, __delete__中的任意一个方法的对象
数据描述符: 对象定义了__get__和__set__
非数据描述符: 只定义了__get__
"""


class TypedProperty(object):
    """type checking on an object attribute using python descriptors"""
    def __init__(self, name, type, default=None):
        self.name = "_" + name
        self.type = type
        self.default = default if default else type()

    def __get__(self, instance, objtype=None):
        return getattr(instance, self.name, self.default)

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError("Must be a %s" % self.type)
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        raise AttributeError("can not delete attribute!")


class Foo(object):
    name = TypedProperty("name", str)
    num = TypedProperty("num", int, 42)


# -------------------property-----------------
class Account(object):
    """adding data descriptors to attributes in python"""
    def __init__(self):
        self._acct_num = None

    def get_acct_num(self):
        print "get acct_num"
        return self._acct_num

    def set_acct_num(self, value):
        print "set acct_num"
        self._acct_num = value

    def del_acct_num(self):
        print "del acct_num"
        del self._acct_num

    acct_num = property(get_acct_num, set_acct_num, del_acct_num, "Account number property")


class TestProperty(object):
    """docstring for TestProperty."""
    def __init__(self):
        self._x = None

    @property
    def x(self):
        print "geting x"
        return self._x

    @x.setter
    def x(self, value):
        print "setting x"
        self._x = value

    @x.deleter
    def x(self):
        print "deleting x"
        del self._x


if __name__ == '__main__':
    foo = Foo()
    foo.name = "testname"
    foo.num = 100
    print foo.name, foo.num
    foo.num = '1000'  # TypeError: Must be a <type 'int'>

    account = Account()
    print account.acct_num  # get acct_num
    account.acct_num = 1000  # set acct_num
    print account.acct_num  # get acct_num

    test_property = TestProperty()
    print test_property.x  # geting x
    test_property.x = 1000  # setting x
    print test_property.x  # geting x
