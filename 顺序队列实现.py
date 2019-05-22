# class node(object):
#     def __init__(self,val):
#         self.val = val

class MyQueue(object):
    def __init__(self,cap):
        self.queue = [None for _ in range(cap)]
        self.cap = cap
        self.count = 0
        self.head = 0
        self.tail = 0
    
    def enqueue(self,val):
        if self.count >= self.cap or val == None:
            return
        if self.tail == self.cap:
            cur = self.head
            i = 0
            while i < self.count:
                self.queue[i] = self.queue[cur]
                self.queue[cur] = None
                i += 1
                cur += 1
            self.head = 0
            self.tail = self.count
        self.queue[self.tail] = val
        self.tail += 1
        self.count += 1
        
                

    def dequeue(self):
        if self.count == 0:
            return
        ret = self.queue[self.head]
        self.queue[self.head] = None
        self.head += 1
        self.count -= 1
        return ret

k = 10
queue = MyQueue(k)

i = 0
while i < k+2:
    queue.enqueue(i)
    i += 1

i = 0
while i < 3:
    queue.dequeue()
    i += 1

print('-----',queue.queue)

queue.enqueue(11)
queue.enqueue(12)
queue.enqueue(13)
queue.enqueue(12)

i = 0
while i < 3:
    queue.dequeue()
    i += 1

queue.enqueue(11)
queue.enqueue(12)
queue.enqueue(13)
queue.enqueue(12)

print('-----',queue.queue)