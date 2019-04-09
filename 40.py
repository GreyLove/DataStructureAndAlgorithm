# #// 面试题40：最小的k个数
# #// 题目：输入n个整数，找出其中最小的k个数。例如输入4、5、1、6、2、7、3、8
# #// 这8个数字，则最小的4个数字是1、2、3、4。


# 少量数据用快排找位置的方法
def GetLeastNumbers_Solution1(data,k):
    if not data or len(data) == 0 or k < 1 or k > len(data):
        return []
    if k == len(data):
        return data
    def position(data,i,j):
        sentry = data[i]
        while i < j :
            while i < j and data[j] >= sentry:
                j -= 1
            
            data[i] = data[j]

            while i < j and data[i] <= sentry:
                i += 1
            
            data[j] = data[i]
        
        data[i] = sentry
        return i
    
    i = 0
    j = len(data)-1
    p = position(data,i,j)
    while p != k:
        if p < k :
            i = p + 1
        else:
            j = p-1
        p =  position(data,i,j)
    
    return data[0:k]

class MaxHeap(object):
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
                if child+1<=self.size() and  self.data[child] < self.data[child+1]:
                    child = child+1
                
                if self.data[root] < self.data[child]:
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
                if child+1 <= self.size() and self.data[child] < self.data[child+1]:
                    child = child + 1
                
                if self.data[root] < self.data[child]:
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


# 大量数据用最大堆
def GetLeastNumbers_Solution2(data,k):
    if not data or len(data) == 0 or k < 1 or k > len(data):
        return []
    if k == len(data):
        return data
    
    heap = MaxHeap()

    for i in data:
        if heap.size() >= k:
            if heap.top()>i:
                heap.pop()
            else:
                continue
        heap.push(i)
    
    return heap.data[1:]

            



#// ====================测试代码====================
def Test(testName, data, n, expectedResult, k):

    if(testName != None):
        print("%s begins: \n"% testName)
    
    print ('1:',GetLeastNumbers_Solution1(data,k))
    print ('2:',GetLeastNumbers_Solution2(data,k))


#// k小于数组的长度
def Test1():

    data = [4, 5, 1, 6, 2, 7, 3, 8]
    expected = [1, 2, 3, 4]
    Test("Test1", data, len(data), expected, len(expected))


#// k等于数组的长度
def Test2():

    data = [4, 5, 1, 6, 2, 7, 3, 8]
    expected = [1, 2, 3, 4, 5, 6, 7, 8]
    Test("Test2", data, len(data), expected, len(expected))


#// k大于数组的长度
def Test3():

    data = [4, 5, 1, 6, 2, 7, 3, 8]
    expected = None
    Test("Test3", data, len(data), expected, 10)


#// k等于1
def Test4():

    data = [4, 5, 1, 6, 2, 7, 3, 8]
    expected = [1]
    Test("Test4", data, len(data), expected, len(expected))


#// k等于0
def Test5():

    data = [4, 5, 1, 6, 2, 7, 3, 8]
    expected = None
    Test("Test5", data, len(data), expected, 0)


#// 数组中有相同的数字
def Test6():

    data = [4, 5, 1, 6, 2, 7, 2, 8]
    expected = [1, 2]
    Test("Test6", data, len(data), expected, len(expected))


#// 输入空指针
def Test7():

    expected = None
    Test("Test7", None, 0, expected, 0)


Test1()
Test2()
Test3()
Test4()
Test5()
Test6()
Test7()

