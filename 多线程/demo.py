import time
import threading

def func1():
    for i in range(5):
        print('---这是func1中i的值--', i)
        time.sleep(1)


def func2():
    for i in range(5):
        print('---这是func2中i的值--', i)
        time.sleep(1)

def single_():
    func1()
    func2()

def multi():
    t1 = threading.Thread(target=func1)
    t2 = threading.Thread(target=func2)
    t1.start()
    t2.start()

if __name__ == '__main__':
    # single_()
    multi()