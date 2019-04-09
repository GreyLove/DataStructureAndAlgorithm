# #// 面试题53（二）：0到n-1中缺失的数字
# #// 题目：一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字
# #// 都在范围0到n-1之内。在范围0到n-1的n个数字中有且只有一个数字不在该数组
# #// 中，请找出这个数字。

def GetMissingNumber(a):
    if not a or len(a) == 0:
        return -1
    
    i = 0 
    j = len(a)-1

    while i <= j:
        m = (i+j)>>1
        if a[m] == m:
            i = m+1
        else:
            if (m == 0 or (m>0 and a[m-1] == m-1)):
                return m
            else:
                j = m-1
    
    return i


# #// ====================测试代码====================
def Test(testName, numbers, length, expected):

    if(testName != None):
        print("%s begins: "% testName)

    result = GetMissingNumber(numbers)
    if(result == expected):
        print("Passed.\n")
    else:
        print("Failed.\n")


#// 缺失的是第一个数字0
def Test1():

    numbers =  [1, 2, 3, 4, 5 ]
    expected = 0
    Test("Test1", numbers, len(numbers), expected)


#// 缺失的是最后一个数字
def Test2():

    numbers =  [0, 1, 2, 3, 4] 
    expected = 5
    Test("Test2", numbers, len(numbers), expected)


#// 缺失的是中间某个数字0
def Test3():

    numbers = [0, 1, 2, 4, 5] 
    expected = 3
    Test("Test3", numbers, len(numbers), expected)


#// 数组中只有一个数字，缺失的是第一个数字0
def Test4():

    numbers = [1] 
    expected = 0
    Test("Test4", numbers, len(numbers), expected)


#// 数组中只有一个数字，缺失的是最后一个数字1
def Test5():

    numbers = [0]
    expected = 1
    Test("Test5", numbers, len(numbers), expected)


#// 空数组
def Test6():

    expected = -1
    Test("Test6", None, 0, expected)


Test1()
Test2()
Test3()
Test4()
Test5()
Test6()
