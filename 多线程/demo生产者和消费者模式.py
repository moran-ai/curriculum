import threading
import random
import time

# 余额
money = 0

# 创建锁对象
lock = threading.Lock()


class Prodeuter(threading.Thread):
    """
    生产者
    """

    def run(self):
        global money
        for _ in range(10):
            lock.acquire()
            # 挣的钱
            m = random.randint(1000, 10000)
            money += m
            print(threading.current_thread().getName(), "挣了多少钱{},当前余额为{}".format(m, money))
            time.sleep(1)
            lock.release()


class Customer(threading.Thread):
    def run(self):
        global money
        for _ in range(10):
            lock.acquire()
            # 花的钱
            m = random.randint(1000, 10000)
            # 如果花的钱小于余额
            if m <= money:
                money -= m
                print(threading.current_thread().getName(), '花了多少钱{},当前余额为{}'.format(m, money))
            else:
                print(threading.current_thread().getName(), '想花{}钱，余额不够，当前余额为{}'.format(m, money))
            time.sleep(1)
            lock.release()


def start():
    for i in range(10):
        t = Prodeuter(name='生产者{}'.format(i))
        t.start()

    for i in range(10):
        cu = Customer(name='----------->消费者{}'.format(i))
        cu.start()


if __name__ == '__main__':
    start()
