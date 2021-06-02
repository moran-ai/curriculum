import threading
import time


class CodingThread1(threading.Thread):
    def run(self):
        # 获取当前线程对象
        thread = threading.current_thread()
        print('CodingThread1的线程对象是---->', thread)
        print('线程的名字为:', thread.getName())
        thread.setName('线程1')
        print('线程的名字为:', thread.getName())
        for i in range(5):
            print('---这是func1中i的值--', i)
            time.sleep(1)


class CodingThread2(threading.Thread):
    def run(self):
        thread = threading.current_thread()
        print('CodingThread2的线程对象是---->', thread)
        print('线程的名字为:', thread.getName())
        thread.setName('线程2')
        print('线程的名字为:', thread.getName())
        for i in range(5):
            print('---这是func2中i的值--', i)
            time.sleep(1)


def mutl():
    t1 = CodingThread1()
    t2 = CodingThread2()
    t1.start()
    t2.start()
    # 获取多个线程的信息
    print(threading.enumerate())


if __name__ == '__main__':
    mutl()
