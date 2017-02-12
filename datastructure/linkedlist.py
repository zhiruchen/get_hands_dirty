# encoding: utf-8


class Node(object):
    """链表结点"""
    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, val):
        self._data = val

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_p):
        self._next = next_p


class LinkedList(object):
    def __init__(self):
        self._head = None
        self._size = 0

    def add(self, data):
        temp = Node(data)
        temp.next = self._head
        self._head = temp
        self._size += 1

    def reverse(self):
        """反转链表"""
        cur = None

        while self._head:
            temp = self._head.next
            self._head.next = cur
            cur = self._head
            self._head = temp

        self._head = cur

    def __iter__(self):
        return self

    def next(self):
        if self._head:
            temp_head = self._head
            self._head = self._head.next
            return temp_head.data

    @staticmethod
    def merge_two_list(node1, node2):
        """merge two sorted linkedlist"""
        if not node1:
            return node1

        if not node2:
            return node2

        if node1.data > node2.data:
            temp = node2
            temp.next = LinkedList.merge_two_list(node1, node2.next)
            return temp
        else:
            temp = node1
            temp.next = LinkedList.merge_two_list(node1.next, node2)
            return temp


def test_link_list():
    linked_list = LinkedList()
    for n in range(5):
        linked_list.add(n)

    # while linked_list._head:
    #     print linked_list._head.data
    #     linked_list._head = linked_list._head.next

    linked_list.reverse()
    while linked_list._head:
        print linked_list._head.data
        linked_list._head = linked_list._head.next
    # for x in linked_list:
    #     print x


def test_merge_two_list():
    linked_list1 = LinkedList()
    for n in range(5):
        linked_list1.add(n)

    linked_list2 = LinkedList()
    for n in range(5, 10):
        linked_list2.add(n)

    final_head = LinkedList.merge_two_list(linked_list1._head, linked_list2._head)
    while final_head:
        print final_head.data
        final_head = final_head.next
