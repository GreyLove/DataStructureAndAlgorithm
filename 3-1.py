# #// 面试题3（一）：找出数组中重复的数字
# #// 题目：在一个长度为n的数组里的所有数字都在0到n-1的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，
# #// 也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。例如，如果输入长度为7的数组2, 3, 1, 0, 2, 5, 3，
# #// 那么对应的输出是重复的数字2或者3。

###请找出数组中任意一个重复的数字!!!!

def duplicate(numbers,length, duplication:list):
    if not numbers or len(numbers) == 0:
        return False
    length = len(numbers)

    for i in range(length):
        if numbers[i] > length-1:
            return False

    for i in range(length):
        if numbers[i] > length-1:
            return False
        while numbers[i] != i:
            if numbers[numbers[i]] ==  numbers[i]:
                find = False
                for du in duplication:
                    if du == numbers[i]:
                        find = True
                        break
                if not find:
                    duplication.append(numbers[i])
                break
            tmp = numbers[numbers[i]]
            numbers[numbers[i]] = numbers[i]
            numbers[i] = tmp

    
    if len(duplication):
        return True
    else:
       duplication.append(-1)
       return False 


    

#// ====================测试代码====================
def contains(array, length, number):
    if len(array) != len(number):
        return False
    for i in range(len(array)):
        if(array[i] == number[i]):
            return True

    return False

def test(testName, numbers, lengthNumbers, expected, expectedExpected, validArgument):

    print("%s begins: "% testName)

    duplication = []
    validInput = duplicate(numbers, lengthNumbers, duplication)

    if(validArgument == validInput):
    
        if(validArgument):
        
            if(contains(expected, expectedExpected, duplication)):
                print("Passed.\n")
            else:
                print("FAILED.\n")
        
        else:
            print("Passed.\n")
    
    else:
        print("FAILED.\n")


#// 重复的数字是数组中最小的数字
def test1():

    numbers =  [2, 1, 3, 1, 4 ]
    duplications =  [1 ]
    test("Test1", numbers, len(numbers), duplications, len(duplications), True)


#// 重复的数字是数组中最大的数字
def test2():

    numbers =  [2, 4, 3, 1, 4 ]
    duplications =  [4 ]
    test("Test2", numbers, len(numbers), duplications, len(duplications), True)


#// 数组中存在多个重复的数字
def test3():

    numbers =  [2, 4, 2, 1, 4 ]
    duplications =  [2, 4 ]
    test("Test3", numbers, len(numbers), duplications, len(duplications), True)


#// 没有重复的数字
def test4():

    numbers =  [2, 1, 3, 0, 4 ]
    duplications =  [-1 ] #// not in use in the test function
    test("Test4", numbers, len(numbers), duplications, len(duplications), False)


#// 没有重复的数字
def test5():

    numbers =  [2, 1, 3, 5, 4 ]
    duplications =  [-1  ]#// not in use in the test function
    test("Test5", numbers, len(numbers), duplications, len(duplications), False)


#// 无效的输入
def test6():
    numbers = None
    duplications =  [-1 ] #// not in use in the test function
    test("Test6", numbers, 0, duplications, len(duplications), False)


# test1()
# test2()
# test3()
# test4()
test5()
test6()
    

