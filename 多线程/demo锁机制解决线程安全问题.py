import threading
import time

# 全局变量
ticker = 100

# 创建锁对象
lock = threading.Lock()


def sale_ticker():
    global ticker
    for i in range(1000):
        lock.acquire()  # 加锁
        if ticker > 0:
            print(threading.current_thread().getName() + '--->正在出售第{}张票'.format(ticker))
            ticker -= 1
        time.sleep(1)
        lock.release()  # 释放锁

def start():
    for i in range(3):
        t1 = threading.Thread(target=sale_ticker)
        t1.start()


if __name__ == '__main__':
    start()
