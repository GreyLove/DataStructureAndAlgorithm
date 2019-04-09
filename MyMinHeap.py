class MinHeap(object):
    def __init__(self):
        self.data = [None]
    
    def push(self,val):
        if val == None:
            return
        self.data.append(val)
        if self.size() > 0:
            root = self.size()>>1
            child = root*2
            while root > 0:
                if child+1<=self.size() and  self.data[child] > self.data[child+1]:
                    child = child+1
                
                if self.data[root] > self.data[child]:
                    tmp = self.data[root]
                    self.data[root] = self.data[child]
                    self.data[child] = tmp
                    child = root
                    root = child >> 1
                else:
                    break
        
    def pop(self):
        if self.size():
            head = self.data[1]
            last = self.data.pop()
            if self.size() == 0:
                return head
            self.data[1] = last
            root = 1
            child = root*2

            while child <= self.size():
                if child+1 <= self.size() and self.data[child] > self.data[child+1]:
                    child = child + 1
                
                if self.data[root] > self.data[child]:
                    tmp = self.data[root]
                    self.data[root] = self.data[child]
                    self.data[child] = tmp
                    root = child
                    child = root*2
                else:
                    break
            return head

    def top(self):
        if self.size()>0:return self.data[1]

    def size(self):
        return len(self.data)-1