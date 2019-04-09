# #// 面试题42：连续子数组的最大和
# #// 题目：输入一个整型数组，数组里有正数也有负数。数组中一个或连续的多个整
# #// 数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为O(n)。

def FindGreatestSumOfSubArray(pData):
    if not pData or len(pData) == 0:
        return 0
    
    maxSum = pData[0]
    s = pData[0]
    for i in range(1,len(pData)):
        s += pData[i]
        if s < pData[i]:
            s = pData[i]

        if s > maxSum:
            maxSum = s
    
    return maxSum
        






#// ====================测试代码====================
def Test(testName, pData, nLength, expected, expectedFlag):

    if(testName != None):
        print("%s begins: \n"% testName)

    result = FindGreatestSumOfSubArray(pData)
    if(result == expected):
        print("Passed.\n")
    else:
        print("Failed.\n")


#// 1, -2, 3, 10, -4, 7, 2, -5
def Test1():

    data = 1, -2, 3, 10, -4, 7, 2, -5
    Test("Test1", data, len(data), 18, False)


#// 所有数字都是负数
#// -2, -8, -1, -5, -9
def Test2():

    data = -2, -8, -1, -5, -9
    Test("Test2", data, len(data), -1, False)


#// 所有数字都是正数
#// 2, 8, 1, 5, 9
def Test3():

    data = 2, 8, 1, 5, 9
    Test("Test3", data, len(data), 25, False)


#// 无效输入
def Test4():

    Test("Test4", None, 0, 0, True)


Test1()
Test2()
Test3()
Test4()
