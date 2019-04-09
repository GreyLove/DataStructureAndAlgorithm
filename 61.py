# #// 面试题61：扑克牌的顺子
# #// 题目：从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
# #// 2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王可以看成任意数字。

def position(num,i,j):
    t = num[i]
    while i < j:
        while i < j and num[j] >= t :
            j -= 1
        num[i] = num[j]

        while i < j and num[i] <= t:
            i += 1 
        num[j] = num[i]
    
    num[i] = t
    return i

def quickSort(num,i,j):
    if i < j:
        m = position(num,i,j)
        quickSort(num,i,m-1)
        quickSort(num,m+1,j)

def IsContinuous(numbers):
    if not numbers or len(numbers) == 0:
        return False
    
    quickSort(numbers,0,len(numbers)-1)

    zore = 0

    for i in range(len(numbers)):
        if numbers[i] == 0:
            zore += 1

    
    for i in range(zore,len(numbers)-1):
        if numbers[i+1] == numbers[i]:
            return False
        c = numbers[i+1] - numbers[i] - 1
        if c>zore:
            return False
        else:
            zore -= c
    
    return True




#// ====================测试代码====================
def Test(testName, numbers, length,  expected):

    if(testName != None):
        print("%s begins: "% testName)

    if(IsContinuous(numbers) == expected):
        print("Passed.\n")
    else:
        print("Failed.\n")


def Test1():

    numbers =  [1, 3, 2, 5, 4] 
    Test("Test1", numbers, 0, True)


def Test2():

    numbers =  [1, 3, 2, 6, 4 ]
    Test("Test2", numbers, 0, False)


def Test3():

    numbers =  [0, 3, 2, 6, 4 ]
    Test("Test3", numbers, 0, True)


def Test4():

    numbers =  [0, 3, 1, 6, 4 ]
    Test("Test4", numbers, 0, False)


def Test5():

    numbers =  [1, 3, 0, 5, 0 ]
    Test("Test5", numbers, 0, True)


def Test6():

    numbers =  [1, 3, 0, 7, 0 ]
    Test("Test6", numbers, 0, False)


def Test7():

    numbers =  [1, 0, 0, 5, 0 ]
    Test("Test7", numbers, 0, True)


def Test8():

    numbers =  [1, 0, 0, 7, 0] 
    Test("Test8", numbers, 0, False)


def Test9():

    numbers =  [3, 0, 0, 0, 0 ]
    Test("Test9", numbers, 0, True)


def Test10():

    numbers =  [0, 0, 0, 0, 0 ]
    Test("Test10", numbers, 0, True)


#// 有对子
def Test11():

    numbers =  [1, 0, 0, 1, 0 ]
    Test("Test11", numbers, 0, False)


#// 鲁棒性测试
def Test12():

    Test("Test12", None, 0, False)


Test1()
Test2()
Test3()
Test4()
Test5()
Test6()
Test7()
Test8()
Test9()
Test10()
Test11()
Test12()
