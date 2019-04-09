# #// 面试题39：数组中出现次数超过一半的数字
# #// 题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例
# #// 如输入一个长度为9的数组1, 2, 3, 2, 2, 2, 5, 4, 2。由于数字2在数组中
# #// 出现了5次，超过数组长度的一半，因此输出2。

# 第一种是快拍找位置的思想

def position(numbers,i,j):
    sentry = numbers[i]
    while i < j:
        while i < j and sentry <= numbers[j]:
            j -= 1
        numbers[i] = numbers[j]

        while i < j and sentry >= numbers[i]:
            i += 1
        numbers[j] = numbers[i]
    
    numbers[i] = sentry

    return i

def MoreThanHalfNum_Solution1(numbers):
    if not numbers or len(numbers) < 1:
        return 0
    
    i = 0
    j = len(numbers)-1
    m = (i+j)>>1

    p = position(numbers,i,j)
    while p != m:
        if p < m:
            i = p+1
        else:
            j = j-1
        p = position(numbers,i,j)
    
    count = 0
    for i in numbers:
        if i == numbers[m]:
            count += 1
    
    if count > len(numbers)>>1:
        return numbers[m]

    return 0




def MoreThanHalfNum_Solution2(numbers):
    if not numbers or len(numbers) < 1:
        return 0
    k = numbers[0]
    c = 1

    for i in range(1,len(numbers)):
        if numbers[i] == k:
            c += 1
        else:
            c -= 1
            if c == 0:
                k = numbers[i]
                c = 1
    
    count = 0
    for i in numbers:
        if i == k:
            count += 1
    
    if count > len(numbers)>>1:
        return k
    
    return 0


#// ====================测试代码====================
def Test(testName, numbers, length, expectedValue, expectedFlag):

    if(testName != None):
        print("%s begins: \n"% testName)

    copy = []
    for i in range(len(numbers)):
        copy.append(numbers[i])
        

    print("Test1 for solution1: ")
    result = MoreThanHalfNum_Solution1(numbers)
    if(result == expectedValue):
        print("Passed.\n")
    else:
        print("Failed.\n")

    print("Test2 for solution2: ")
    result = MoreThanHalfNum_Solution2(copy)
    if(result == expectedValue):
        print("Passed.\n")
    else:
        print("Failed.\n")


#// 存在出现次数超过数组长度一半的数字
def Test1():

    numbers = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    Test("Test1", numbers, 0, 2, False)


#// 不存在出现次数超过数组长度一半的数字
def Test2():

    numbers = [1, 2, 3, 2, 4, 2, 5, 2, 3]
    Test("Test2", numbers, 0, 0, True)


#// 出现次数超过数组长度一半的数字都出现在数组的前半部分
def Test3():

    numbers = [2, 2, 2, 2, 2, 1, 3, 4, 5]
    Test("Test3", numbers, 0, 2, False)


#// 出现次数超过数组长度一半的数字都出现在数组的后半部分
def Test4():

    numbers = [1, 3, 4, 5, 2, 2, 2, 2, 2]
    Test("Test4", numbers, 0, 2, False)


#// 输入空指针
def Test5():

   numbers = [1]
   Test("Test5", numbers, 1, 1, False)


#// 输入空指针
def Test6():

    Test("Test6", None, 0, 0, True)


Test1()
Test2()
Test3()
Test4()
Test5()
# Test6()
