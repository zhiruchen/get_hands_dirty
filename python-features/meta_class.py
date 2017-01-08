# -*- encoding: utf-8 -*-

"""
元类：用于创建类的类
python中一切都是对象，类是type类的对象
https://jakevdp.github.io/blog/2012/12/01/a-primer-on-python-metaclasses/
"""


# --------------------修改类属性--------------------
class MyClass(object):
    pass


class InterfaceMeta(type):
    def __new__(cls, name, bases, attrs):
        if "class_id" not in attrs:
            attrs["class_id"] = name.lower()

        if "file" in attrs:
            filename = attrs["file"]
            attrs["file"] = open(filename, 'w')

        return super(InterfaceMeta, cls).__new__(cls, name, bases, attrs)


class Interface(object):
    __metaclass__ = InterfaceMeta
    file = "temp.txt"

class UserInterface(Interface):
    file = "foo.txt"


def test_interface():
    assert Interface.class_id == "interface"
    assert isinstance(Interface.file, file) is True


def test_userinterface():
    assert UserInterface.class_id == "userinterface"
    assert isinstance(UserInterface.file, file) is True


# ----------------------------注册子类----------------------
class DBInterfaceMeta(type):
    """docstring for DBInterfaceMeta."""
    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, "registry"):
            cls.registry = {}
        else:
            interface_id = name.lower()
            cls.registry[interface_id] = cls  # 注册继承的子类
        super(DBInterfaceMeta, cls).__init__(name, bases, attrs)


class DBInterface(object):
    __metaclass__ = DBInterfaceMeta


class FirstInterface(DBInterface):
    pass


class SecondInterface(DBInterface):
    pass


def test_dbinterface():
    assert DBInterface.registry['firstinterface'] is FirstInterface
    assert DBInterface.registry['secondinterface'] is SecondInterface


if __name__ == '__main__':
    test_interface()
    test_userinterface()
    test_dbinterface()
