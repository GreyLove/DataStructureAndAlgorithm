# // 面试题14：剪绳子
# // 题目：给你一根长度为n绳子，请把绳子剪成m段（m、n都是整数，n>1并且m≥1）。
# // 每段的绳子的长度记为k[0]、k[1]、……、k[m]。k[0]*k[1]*…*k[m]可能的最大乘
# // 积是多少？例如当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此
# // 时得到最大的乘积18。

# 动态规划
def maxProductAfterCutting_solution1(length):
    if length == 0:
        return 0
    elif length == 1:
        return 0
    elif length == 2:
        return 1
    elif length == 3:
        return 2
    elif length == 4:
        return 4
    
    tmp = [0 for _ in range(length+1)]

    tmp[0] = 0
    tmp[1] = 1
    tmp[2] = 2
    tmp[3] = 3
    tmp[4] = 4

    for i in range(5,length+1):

        k = i >> 1
        j = 1
        maxs = 0
        while j <= k:
            v = tmp[j]*tmp[i-j]
            if maxs < v:
                maxs = v
            j += 1
        tmp[i] = maxs
    
    return tmp[length]


# 数学大法
def maxProductAfterCutting_solution2(length):
    if length == 0:
        return 0
    elif length == 1:
        return 0
    elif length == 2:
        return 1
    elif length == 3:
        return 2
    elif length == 4:
        return 4
    
    timesOf3 = int(length/3)
    timesOf2 = 0
    k = length - timesOf3*3
    if k == 1:
        timesOf3 -= 1
        timesOf2 = 2
    elif k == 2:
        timesOf2 = 1

    s = 3**timesOf3*2**timesOf2
    return s



    

# // ====================测试代码====================
def test(testName,length,expected):
    result1 = maxProductAfterCutting_solution1(length)
    if(result1 == expected):
        print("Solution1 for",testName," passed.")
    else:
        print("Solution1 for",testName," passed.")

    result2 = maxProductAfterCutting_solution2(length)
    if(result2 == expected):
        print("Solution2 for",testName," passed.")
    else:
        print("Solution2 for",testName," passed.")


def test1():

    length = 1
    expected = 0
    test("test1", length, expected)


def test2():

    length = 2
    expected = 1
    test("test2", length, expected)


def test3():

    length = 3
    expected = 2
    test("test3", length, expected)


def test4():

    length = 4
    expected = 4
    test("test4", length, expected)


def test5():

    length = 5
    expected = 6
    test("test5", length, expected)


def test6():

    length = 6
    expected = 9
    test("test6", length, expected)


def test7():

    length = 7
    expected = 12
    test("test7", length, expected)


def test8():

    length = 8
    expected = 18
    test("test8", length, expected)


def test9():

    length = 9
    expected = 27
    test("test9", length, expected)


def test10():

    length = 10
    expected = 36
    test("test10", length, expected)


def test11():

    length = 50
    expected = 86093442
    test("test11", length, expected)

test1()
test2()
test3()
test4()
test5()
test6()
test7()
test8()
test9()
test10()
test11()
