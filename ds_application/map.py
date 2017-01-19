# encoding: utf-8


class Map(object):
    def __init__(self):
        self._size = 11
        self._slots = [None] * self._size

    def hash_func(self, key):
        return hash(key) % self._size

    def put(self, key, val):
        index = self.hash_func(key)
        slot = self._slots[index]
        if slot is None:
            self._slots[index] = [(key, val)]
        else:
            pos = -1
            for p, val in enumerate(slot):
                if key == val[0]:
                    pos = p
                    break
            if pos != -1:
                slot[pos] = ((key, val))
            else:
                slot.append((key, val))
                self._slots[index] = slot

    def get(self, key, default=None):
        index = self.hash_func(key)
        slot = self._slots[index]
        if not slot:
            return default

        for item in slot:
            if key == item[0]:
                return item[1]
        return default


def test_map():
    map = Map()
    map.put('a', 1)
    map.put('b', 2)
    map.put('c', 3)

    print map.get('a', None) == 1
    print map.get('b') == 2
    print map.get('c') == 3
