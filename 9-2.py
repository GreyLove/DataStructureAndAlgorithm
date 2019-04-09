# // 面试题9：两个队列实现一个栈

class GLStack(object):
    
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    
    def push(self,val):
        if val == None:
            return
        if len(self.queue1):
            self.queue1.append(val)
        else:
            self.queue2.append(val)
    
    def pop(self):
        if not self.empty():
            if len(self.queue1):
                while len(self.queue1) > 1:
                    self.queue2.append(self.queue1.pop(0))
                return self.queue1.pop(0)
            else:
                while len(self.queue2) > 1:
                    self.queue1.append(self.queue2.pop(0))
                return self.queue2.pop(0)

    def empty(self):
        return not len(self.queue1) and not len(self.queue2)

s = GLStack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)


while not s.empty():
    print(s.pop())