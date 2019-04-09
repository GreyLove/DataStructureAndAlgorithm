# // 面试题48：最长不含重复字符的子字符串
# // 题目：请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子
# // 字符串的长度。假设字符串中只包含从'a'到'z'的字符。

# 最笨的方法就是两个指针，i j ,j 向后移动。每次移动去j 之前去判断有没有重复，倒着判断，

def longestSubstringWithoutDuplication_1(input1):
    if not input1 or len(input1) == 0:
        return 0

    m = {}
    m[input1[0]] = 0
    maxCount = 1
    count = 1

    for i in range(1,len(input1)):
        if input1[i] in m.keys():
            d = i - m[input1[i]]
            if d <= count:
                count = d
            else:
                count += 1
        else:
            count += 1
        m[input1[i]] = i

        if count > maxCount:
            maxCount = count

    return maxCount

            
    

# // ====================测试代码====================
def testSolution1(input1, expected):

    output = longestSubstringWithoutDuplication_1(input1)
    if(output == expected):
        print("Solution 1 passed, with input1: " , input1)
    else:
        print("Solution 1 FAILED, with input1: " , input1)


# def testSolution2(input1, expected):
#     output = longestSubstringWithoutDuplication_2(input1)
#     if(output == expected):
#         print("Solution 2 passed, with input1: " , input1)
#     else:
#         print("Solution 2 FAILED, with input1: " , input1)


def test(input1, expected):

    testSolution1(input1, expected)
    # testSolution2(input1, expected)


def test1():

    input1 = "abcacfrar"
    expected = 4
    test(input1, expected)


def test2():

    input1 = "acfrarabc"
    expected = 4
    test(input1, expected)


def test3():

    input1 = "arabcacfr"
    expected = 4
    test(input1, expected)


def test4():

    input1 = "aaaa"
    expected = 1
    test(input1, expected)


def test5():

    input1 = "abcdefg"
    expected = 7
    test(input1, expected)


def test6():

    input1 = "aaabbbccc"
    expected = 2
    test(input1, expected)


def test7():

    input1 = "abcdcba"
    expected = 4
    test(input1, expected)


def test8():

    input1 = "abcdaef"
    expected = 6
    test(input1, expected)


def test9():

    input1 = "a"
    expected = 1
    test(input1, expected)


def test10():

    input1 = ""
    expected = 0
    test(input1, expected)

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
