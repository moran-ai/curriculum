import time
from queue import Queue

# 创建一个队列,这个队列最多可以存放5个数据
q = Queue(5)

# 向队列中存放数据
for i in range(4):
    q.put(i)
print('队列中的实际数据为：', q.qsize())

# 取出队列中的数据
for _ in range(5):
    try:
        # block=False 不需要阻塞
        print(q.get(block=False))
    except:
        print('数据已经取完，队列为空')
        break

if q.full():
    print('队列已满')
else:
    print('队列未满，队列的个数为:', q.qsize())

print('-------------------')

q2 = Queue(5)
for i in range(6):
    try:
        q2.put(i, block=False)
    except:
        print('队列已满')
        break
