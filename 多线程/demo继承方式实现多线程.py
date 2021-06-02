import threading
import time

class CodingThread1(threading.Thread):
    def run(self):
        for i in range(5):
            print('---这是func1中i的值--', i)
            time.sleep(1)

class CodingThread2(threading.Thread):
    def run(self):
        thread = threading.current_thread()
        print('线程名字：', thread.getName())
        print(threading.enumerate())
        for i in range(5):
            print('---这是func2中i的值--', i)
            time.sleep(1)

def mutl():
    t1 = CodingThread1()
    t2= CodingThread2()
    t1.start()
    t2.start()

if __name__ == '__main__':
    mutl()
