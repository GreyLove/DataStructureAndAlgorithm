# #// 面试题66：构建乘积数组
# #// 题目：给定一个数组A[0, 1, …, n-1]，请构建一个数组B[0, 1, …, n-1]，其
# #// 中B中的元素B[i] =A[0]×A[1]×… ×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

def BuildProductionArray(A):
    if not A or len(A) == 0:
        return None
    
    n = len(A)
    fb = [1 for _ in range(n)]
    fc = [1 for _ in range(n)]

    for i in range(1,n):
        fb[i] = fb[i-1]*A[i-1]
    
    i = n-2
    while i >= 0:
        fc[i] = fc[i+1]*A[i+1]
        i -= 1

    for i in range(0,n):
        fb[i] = fb[i]*fc[i]
    
    return fb




#//================= Test Code =================
def EqualArrays(input1,output):

    length1 = len(input1)
    length2 = len(output)

    if(length1 != length2):
        return False

    for i in range(length1):
        if(input1[i] != output[i]):
            return False

    return True

def test(testName, input1, output, expected):

    print("%s Begins: ", testName)

    output = BuildProductionArray(input1)
    if(EqualArrays(output, expected)):
        print("Passed.\n")
    else:
        print("FAILED.\n")

def test1():

    #// 输入数组中没有0
    input1 = [ 1, 2, 3, 4, 5 ]
    output = [ 0, 0, 0, 0, 0 ]
    expected = [ 120, 60, 40, 30, 24 ]

    test("Test1",input1,output,expected)


def test2():

    #// 输入数组中有一个0
    input1 = [ 1, 2, 0, 4, 5 ]
    output = [ 0, 0, 0, 0, 0 ]
    expected = [ 0, 0, 40, 0, 0 ]

    test("Test2",input1,output,expected)


def test3():

    #// 输入数组中有两个0
    input1 = [ 1, 2, 0, 4, 0 ]
    output = [ 0, 0, 0, 0, 0 ]
    expected = [ 0, 0, 0, 0, 0 ]

    test("Test3",input1,output,expected)


def test4():

    #// 输入数组中有正、负数
    input1 = [ 1, -2, 3, -4, 5 ]
    output = [ 0, 0, 0, 0, 0 ]
    expected = [ 120, -60, 40, -30, 24 ]

    test("Test4",input1,output,expected)


def test5():

    #// 输入输入中只有两个数字
    input1 = [ 1, -2 ]
    output = [ 0, 0 ]
    expected = [ -2, 1 ]

    test("Test5",input1,output,expected)


test1()
test2()
test3()
test4()
test5()
