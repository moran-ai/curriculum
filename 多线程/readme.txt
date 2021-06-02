类创建线程对象
    class CodingThread1(threading.Thread):
    def run(self):
        for i in range(5):
            print('---这是func1中i的值--', i)
            time.sleep(1)

    class CodingThread2(threading.Thread):
        def run(self):
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

常用方法：
    获取当前线程对象   threading.current_thread()
    获取当前运行的N多线程信息  threading.enumerate()
    获取线程名称  getName()
    设置线程名称  setName()

锁机制
threading.Lock类
    ① 为了解决多线程访问全局变量多造成的安全性问题可以采用锁机制
    ② 访问全局变量无需加锁
    ③ 修改全局变量时才需要加锁，修改完毕后释放锁

加锁的步骤
    ① 创建锁对象
        threading.Lock()
    ② 加锁
        .acquire()

    ③ 释放锁
        .release()

生产者和消费者
    生产者和消费者模式是多线程开发中常见的一种模式
    生产者线程：
        生产者线程用于'生产'数据
    消费者线程
        消费者线程用于'消费'数据

线程间的通信
    acquire() 加锁
    release() 解锁
    wait() 将当前线程处于等待状态，并且释放锁。可以被其他线程使用notify()和notify_all()唤醒。
        被唤醒后继续等待上锁，上锁后继续执行下面的代码
    notify() 通知某个正在等待的线程，默认是第一个等待的线程
    notify_all() 通知所有等待的线程.notify()和notify_all()需要在release()【解锁】之前调用

队列
    FIFO(先进先出) 队列Queue
    LIFO(后进先出) LifoQueue

    函数:
        qsize() 返回队列大小
        empty() 判断队列是否为空
        full()  判断队列是否满
        get()   从队列中取出最先插入的数据
        put()   将一个数据放入队列中

python多线程的GIL锁
GIL锁和Lock锁
    GIL:可以保证全局同一时刻只有一个线程在执行，但是不能保证执行代码的原子性
    Lock:多个线程访问全局变量时数据的安全性

