class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def enqueue(self,val):
        if val == None:
            return
        node = Node(val)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        
        self.count += 1
    
    def dequeue(self):
        if self.count == 0:
            return
        ret = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = ret.next
        ret.next = None
        self.count -= 1
        return ret


k = 5
queue = MyLinkQueue()
for i in range(1,k):
    queue.enqueue(i)

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.enqueue(5)
queue.dequeue()
queue.dequeue()
print(queue)