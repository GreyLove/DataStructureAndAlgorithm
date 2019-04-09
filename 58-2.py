# #// 面试题58（二）：左旋转字符串
# #// 题目：字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
# #// 请定义一个函数实现字符串左旋转操作的功能。比如输入字符串"abcdefg"和数
# #// 字2，该函数将返回左旋转2位得到的结果"cdefgab"。

def LeftRotateString(s, num):
    if not s or len(s) == 0 or num<0 or num>len(s):
        return ""

    s1 = list(s)
    
    def reverse(a,i,j):
        while i < j:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
            i += 1
            j -= 1

    reverse(s1,0,len(s1)-1)

    m = len(s1)-num

    reverse(s1,0,m-1)
    reverse(s1,m,len(s1)-1)

    return ''.join(s1)


     



#// ====================测试代码====================
def Test(testName, input1,  num, expectedResult):

    if(testName != None):
        print("%s begins: "% testName)

    result = LeftRotateString(input1, num)

    if((input1 == None and expectedResult == None) or (input1 != None and result == expectedResult)):
        print("Passed.\n\n")
    else:
        print("Failed.\n\n")


#// 功能测试
def Test1():

    input1 = "abcdefg"
    expected = "cdefgab"

    Test("Test1", input1, 2, expected)


#// 边界值测试
def Test2():

    input1 = "abcdefg"
    expected = "bcdefga"

    Test("Test2", input1, 1, expected)


#// 边界值测试
def Test3():

    input1 = "abcdefg"
    expected = "gabcdef"

    Test("Test3", input1, 6, expected)


#// 鲁棒性测试
def Test4():

    Test("Test4", None, 6, None)


#// 鲁棒性测试
def Test5():

    input1 = "abcdefg"
    expected = "abcdefg"

    Test("Test5", input1, 0, expected)


#// 鲁棒性测试
def Test6():

    input1 = "abcdefg"
    expected = "abcdefg"

    Test("Test6", input1, 7, expected)


Test1()
Test2()
Test3()
Test4()
Test5()
Test6()
