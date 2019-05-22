class MyCircleQueue(object):
    def __init__(self,cap):
        self.queue = [None for _ in range(cap)]
        self.head = 0
        self.tail = 0
        self.count = 0
        self.cap = cap
    
    def enqueue(self,val):
        if val == None:
            return
        if self.count >= self.cap:
            return
        #队列满了
        # if (self.tail+1)%self.cap == self.head:
        #     return

        self.queue[self.tail] = val
        self.tail = (self.tail+1)%self.cap
        self.count += 1
    
    def dequeue(self):
        if self.count == 0:
            return
        #队列是空的
        # if self.tail == self.head:
        #     return
        ret = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head+1)%self.cap
        self.count -= 1
        return ret

# 判断满 空 可以有多种解法
q = MyCircleQueue(10)

for i in range(10):
    q.enqueue(i)

print(q.queue)

q.dequeue()    
q.dequeue()

q.enqueue(11)
q.enqueue(12)
q.enqueue(13)

q.dequeue()    
q.dequeue()    
q.dequeue()
q.dequeue()    
q.dequeue()
q.dequeue()    
q.dequeue()
q.dequeue()    
q.dequeue()
q.dequeue()

print(q.queue)
