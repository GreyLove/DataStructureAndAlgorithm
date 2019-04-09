# #// 面试题31：栈的压入、弹出序列
# #// 题目：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是
# #// 否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1、2、3、4、
# #// 5是某栈的压栈序列，序列4、5、3、2、1是该压栈序列对应的一个弹出序列，但
# #// 4、3、5、1、2就不可能是该压栈序列的弹出序列。

def IsPopOrder(pPush, pPop):
    if pPush == None or pPop == None:
        return False
    if len(pPush) != len(pPop) or  (len(pPush) == 0 and len(pPop) == 0):
        return False
    
    statck = []

    i = 0
    j = 0

    while i<len(pPush):
        statck.append(pPush[i])
        while len(statck) and statck[-1] == pPop[j]:
            statck.pop()
            j += 1
        i += 1
    
    if len(statck):
        return False
    
    return True
                    




#// ====================测试代码====================
def Test(testName,pPush, pPop,  nLength,  expected):

    if(testName != None):
        print("%s begins: " % testName)

    if(IsPopOrder(pPush, pPop) == expected):
        print("Passed.\n")
    else:
        print("failed.\n")


def Test1():

    nLength = 5
    push = [1, 2, 3, 4, 5]
    pop = [4, 5, 3, 2, 1]
    
    Test("Test1", push, pop, nLength, True)


def Test2():

    nLength = 5
    push = [1, 2, 3, 4, 5]
    pop = [3, 5, 4, 2, 1]
    
    Test("Test2", push, pop, nLength, True)


def Test3():

    nLength = 5
    push = [1, 2, 3, 4, 5]
    pop = [4, 3, 5, 1, 2]
    
    Test("Test3", push, pop, nLength, False)


def Test4():

    nLength = 5
    push = [1, 2, 3, 4, 5]
    pop = [3, 5, 4, 1, 2]
    
    Test("Test4", push, pop, nLength, False)


#// push和pop序列只有一个数字
def Test5():

    nLength = 1
    push = [1]
    pop = [2]

    Test("Test5", push, pop, nLength, False)


def Test6():

    nLength = 1
    push = [1]
    pop = [1]

    Test("Test6", push, pop, nLength, True)


def Test7():

    Test("Test7", None, None, 0, False)

 
Test1()
Test2()
Test3()
Test4()
Test5()
Test6()
Test7()
