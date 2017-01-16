# encoding: utf-8

"""
整型转字符串
"""
NUM_STR_MAP = {n: str(n) for n in range(10)}


def to_str(num):
    if num < 10:
        return NUM_STR_MAP[num]

    return to_str(num//10) + NUM_STR_MAP[num%10]
