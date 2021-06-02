import threading
import time
import random
from queue import Queue


def add_value(q):
    while True:
        q.put(random.randint(100, 1000))
        time.sleep(1)


def get_value(q):
    while True:
        print('取出来的元素是{}'.format(q.get()))


def start():
    q = Queue(10)
    t1 = threading.Thread(target=add_value, args=(q,))
    t2 = threading.Thread(target=get_value, args=(q,))
    t1.start()
    t2.start()

if __name__ == '__main__':
    start()

