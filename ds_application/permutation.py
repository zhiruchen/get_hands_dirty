# encoding: utf-8

"""
排列组合
"""


def permutation(array):
    """
    abc => abc acb bac bca cab cba
    :param array:
    :return:
    """
    def _permutation(seq, start):
        if start == len(seq) - 1:
            print ''.join(seq)

        i = start
        while i < len(seq):
            seq[i], seq[start] = seq[start], seq[i]
            _permutation(seq, start + 1)
            seq[i], seq[start] = seq[start], seq[i]
            i += 1

    _permutation(array, 0)


def test_permutation():
    array = list("abcd")
    permutation(array)
