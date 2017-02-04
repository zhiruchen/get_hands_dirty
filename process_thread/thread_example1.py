# encoding: utf-8

import threading

"""
python 多线程
"""


count = 0


def incr_count():
    global count
    for _ in xrange(100*100):
        count += 1


def dec_count():
    global count
    for _ in xrange(100*100):
        count -= 1


def main():
    t1 = threading.Thread(target=incr_count)
    t2 = threading.Thread(target=dec_count)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    global count
    print "count=", count


if __name__ == '__main__':
    main()
