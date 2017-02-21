
import random
import heapq
import datetime

l = []
for i in range(1,10000):
    l.append(random.randint(1, 10000))

t1 = datetime.datetime.now()
nums = heapq.nlargest(3,l)
t2 = datetime.datetime.now()
print('method 1, time: %d' % (t1-t2).microseconds)
print(nums)

t1 = datetime.datetime.now()
heap = list(l)
heapq.heapify(heap)
print heapq.heappop(heap)
print heapq.heappop(heap)
print heapq.heappop(heap)
t2 = datetime.datetime.now()
print('method 2, time: %d' % (t1-t2).microseconds)
