# // 面试题9：用两个栈实现队列
# // 题目：用两个栈实现一个队列。队列的声明如下，请实现它的两个函数appendTail
# // 和deleteHead，分别完成在队列尾部插入结点和在队列头部删除结点的功能。

class GLQueue(object):
    def __init__(self):
        self.inStack = []
        self.outStack = []
    
    def push(self,val):
        if val:
            self.inStack.append(val)
    
    def pop(self):
        if not self.empty():
            if len(self.outStack):
                return self.outStack.pop()
            else:
                while len(self.inStack):
                    self.outStack.append(self.inStack.pop())
                
                return self.outStack.pop()

    
    def empty(self):
        return  len(self.inStack) == 0 and len(self.outStack) == 0
    

q = GLQueue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)

while not q.empty():
    print(q.pop())