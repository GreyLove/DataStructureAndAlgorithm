# #// 面试题63：股票的最大利润
# #// 题目：假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖交易该股
# #// 票可能获得的利润是多少？例如一只股票在某些时间节点的价格为9, 11, 8, 5,
# #// 7, 12, 16, 14。如果我们能在价格为5的时候买入并在价格为16时卖出，则能
# #// 收获最大的利润11。


def MaxDiff(numbers):
    if not numbers or len(numbers) < 2:
        return 0
    
    i = 0
    j = 1
    maxDiff = numbers[j]-numbers[i]
    while j < len(numbers):
        m = numbers[j]-numbers[i]
        if maxDiff < m:
            maxDiff = m
        if numbers[j] < numbers[i]:
            i = j
        j += 1

    
    return maxDiff
        



def Test(testName, numbers, length, expected):

    if(testName != None):
        print("%s begins: "% testName)

    if(MaxDiff(numbers) == expected):
        print("Passed.\n")
    else:
        print("FAILED.\n")


def Test1():

    numbers = [ 4, 1, 3, 2, 5 ]
    Test("Test1", numbers, 0, 4)


#// 价格递增
def Test2():

    numbers = [ 1, 2, 4, 7, 11, 16 ]
    Test("Test2", numbers, 0, 15)


#// 价格递减
def Test3():

    numbers = [ 16, 11, 7, 4, 2, 1 ]
    Test("Test3", numbers, 0, -1)


#// 价格全部相同
def Test4():

	numbers = [ 16, 16, 16, 16, 16 ]
	Test("Test4", numbers, 0, 0)


def Test5():

    numbers = [ 9, 11, 5, 7, 16, 1, 4, 2 ]
    Test("Test5", numbers, 0, 11)


def Test6():

    numbers = [ 2, 4 ]
    Test("Test6", numbers, 0, 2)


def Test7():

    numbers = [ 4, 2 ]
    Test("Test7", numbers, 0, -2)


def Test8():

	Test("Test8", None, 0, 0)


Test1()
Test2()
Test3()
Test4()
Test5()
Test6()
Test7()
Test8()
