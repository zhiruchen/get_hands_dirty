# encoding: utf-8

import threading
import time

"""
python thread
"""


class ThreadTest(threading.Thread):
    """docstring for ThreadTest."""
    def __init__(self, name, delay):
        super(ThreadTest, self).__init__()
        self.name = name
        self.delay = delay

    def run(self):
        print "%s delay for %s" % (self.name, self.delay)
        time.sleep(self.delay)
        c = 0
        while True:
            print "Thread %s on line %s" % (self.name, c)
            c += 1
            if c == 3:
                print "Thread %s end" % self.name
                break


def test_thread():
    t1 = ThreadTest('Thread 1', 2)
    t2 = ThreadTest("Thread 2", 2)
    t1.start()
    print "wait t1 to end"
    t1.join()  # 阻赛主线程执行后面的表达式，直到t1结束
    t2.start()
    print "thread t2 end"


if __name__ == '__main__':
    test_thread()
