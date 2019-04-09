# 队列的最大值，max、push_back、pop_front。时间复杂度都是O(1)
from collections import deque

class QueueData(object):
    def __init__(self,val,index):
        self.val = val
        self.index = index

class MaxQueue(object):

    def __init__(self):
        self.queue = deque()
        self.maxQueue = deque()
        self.index = 0
        

    def push_back(self,val):
        if not val:
            return
        data = QueueData(val,self.index)
        self.queue.append(data)
        while len(self.maxQueue) and val >= self.maxQueue[-1].val:
            self.maxQueue.pop()
        self.maxQueue.append(data)
        self.index += 1

    def pop_front(self):
        if self.size()>0:
            pop = self.queue.popleft()
            if pop.index == self.maxQueue[0].index:
                self.maxQueue.popleft()
            return pop
    
    def Max(self):
        if self.size()>0:
            return self.maxQueue[0].val
    
    def size(self):
        return len(self.queue)


q = MaxQueue()
q.push_back(5)
q.push_back(2)
q.push_back(3)
q.push_back(6)
q.push_back(1)


q.pop_front()
q.pop_front()
q.pop_front()
q.pop_front()

print(q.Max())
