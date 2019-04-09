# #// 面试题53（三）：数组中数值和下标相等的元素
# #// 题目：假设一个单调递增的数组里的每个元素都是整数并且是唯一的。请编程实
# #// 现一个函数找出数组中任意一个数值等于其下标的元素。例如，在数组-3, -1,
# #// 1, 3, 5中，数字3和它的下标相等。

def GetNumberSameAsIndex(numbers):
    if not numbers or len(numbers) == 0:
        return -1
    
    i = 0
    j = len(numbers)

    while i <= j:
        m = (i+j)>>1
        if numbers[m] == m:
            return m
        elif numbers[m] < m:
            i = m+1
        elif numbers[m] > m:
            j = m-1
    
    return -1



# // ====================测试代码====================
def Test(testName, numbers, length, expected):

    if(GetNumberSameAsIndex(numbers) == expected):
        print("%s passed.\n"% testName)
    else:
        print("%s FAILED.\n"% testName)


def Test1():

    numbers = [ -3, -1, 1, 3, 5 ]
    expected = 3
    Test("Test1", numbers, len(numbers), expected)


def Test2():

    numbers = [ 0, 1, 3, 5, 6 ]
    expected = 0
    Test("Test2", numbers, len(numbers), expected)


def Test3():

    numbers = [ -1, 0, 1, 2, 4 ]
    expected = 4
    Test("Test3", numbers, len(numbers), expected)


def Test4():

    numbers = [ -1, 0, 1, 2, 5 ]
    expected = -1
    Test("Test4", numbers, len(numbers), expected)


def Test5():

    numbers = [ 0 ]
    expected = 0
    Test("Test5", numbers, len(numbers), expected)


def Test6():

    numbers = [ 10 ]
    expected = -1
    Test("Test6", numbers, len(numbers), expected)


def Test7():

    Test("Test7", None, 0, -1)


Test1()
Test2()
Test3()
Test4()
Test5()
Test6()
Test7()

