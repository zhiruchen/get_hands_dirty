# encoding: utf-8

"""
lru test
"""

import unittest

from lru import Cache


class TestLRU(unittest.TestCase):
    def test_add(self):
        cache = Cache(4)
        self.assertListEqual([], cache.ll)

        cache.add(1, 1)
        cache.add(2, 2)
        cache.add(3, 3)
        cache.add(4, 4)
        self.assertListEqual([4,3,2,1], cache.ll)

        v, _ = cache.get(1)
        self.assertEqual(1, v)
        self.assertListEqual([1,4,3,2], cache.ll)

        v, _ = cache.get(2)
        self.assertEqual(2, v)
        self.assertListEqual([2,1,4,3], cache.ll)

        cache.add(5, 5)
        self.assertListEqual([5,2,1,4], cache.ll)

        cache.add(1, 1)
        self.assertListEqual([1,5,2,4], cache.ll)

        cache.add(2, 2)
        self.assertListEqual([2,1,5,4], cache.ll)

        cache.add(3, 3)
        self.assertListEqual([3,2,1,5], cache.ll)

        cache.add(4, 4)
        self.assertListEqual([4,3,2,1], cache.ll)

        cache.add(5, 5)
        self.assertListEqual([5,4,3,2], cache.ll)


if __name__ == '__main__':
    unittest.main()