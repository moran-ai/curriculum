import threading
import random
import time

# 余额
money = 0

# 创建Condition对象
lock = threading.Condition()
g_time = 0


class Prodeuter(threading.Thread):
    """
    生产者
    """

    def run(self):
        global money
        global g_time
        for _ in range(10):
            lock.acquire()
            # 挣的钱
            m = random.randint(1000, 10000)
            money += m
            g_time += 1
            print(threading.current_thread().getName(), "挣了多少钱{},当前余额为{}".format(m, money))
            lock.notify_all()  # 释放所有等待的线程
            lock.release()


class Customer(threading.Thread):
    def run(self):
        global money
        for _ in range(10):
            lock.acquire()
            # 花的钱
            m = random.randint(1000, 10000)
            # 如果余额小于花的钱
            while money < m:
                # 消费的时间大于赚钱的时间
                if g_time >= 100:
                    # 如果生产者已经没有能力继续赚钱，就释放锁，停止程序
                    lock.release()
                    return
                print(threading.current_thread().getName(), '想花{}钱，但是余额不足，余额为{}'.format(m, money))
                # 线程等待
                lock.wait()  # 余额不足的情况，需要等待生产者赚钱

            # 余额充足，开始花钱
            money -= m
            print(threading.current_thread().getName(), '--------->花了{}钱，当前余额为{}'.format(m, money))
            lock.release()


def start():
    # 10个生产者线程
    for i in range(10):
        t = Prodeuter(name='生产者{}'.format(i))
        t.start()

    # 10个消费者线程
    for i in range(10):
        cu = Customer(name='----------->消费者{}'.format(i))
        cu.start()


if __name__ == '__main__':
    start()
