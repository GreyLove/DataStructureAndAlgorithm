
# // 面试题30：包含min函数的栈
# // 题目：定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min
# // 函数。在该栈中，调用min、push及pop的时间复杂度都是O(1)。

class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min = []
    
    def push(self,val):
        if val != None:
            self.stack.append(val)
            if len(self.min) == 0 or self.min[-1] > val:
                self.min.append(val)
            elif self.min[-1] < val:
                self.min.append(self.min[-1])  
    
    def pop(self):
        if len(self.stack):
            self.stack.pop()
            self.min.pop()
    
    def mins(self):
        return self.min[-1] if len(self.min) else -1



def Test(testName,stack,expected):

    if(testName != None):
        print("%s begins: " % testName)

    if(stack.mins() == expected):
        print("Passed.\n")
    else:
        print("Failed.\n")


stack = MinStack()

stack.push(3)
Test("Test1", stack, 3)

stack.push(4)
Test("Test2", stack, 3)

stack.push(2)
Test("Test3", stack, 2)

stack.push(3)
Test("Test4", stack, 2)

stack.pop()
Test("Test5", stack, 2)

stack.pop()
Test("Test6", stack, 3)

stack.pop()
Test("Test7", stack, 3)

stack.push(0)
Test("Test8", stack, 0)
