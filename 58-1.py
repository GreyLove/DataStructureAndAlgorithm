# #// 面试题58（一）：翻转单词顺序
# #// 题目：输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
# #// 为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，
# #// 则输出"student. a am I"。


def ReverseSentence(s:str)->str:
    if not s or len(s) == 0:
        return s
    s1 = list(s)
    def reverse(a,i,j):
        while i < j:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
            i += 1
            j -= 1
    

    reverse(s1,0,len(s1)-1)

    i = 0
    j = 0
    while j < len(s1):
        if s1[i] == ' ' and s1[j] == ' ':
            i += 1
            j += 1
        elif s1[j] == ' ':
            reverse(s1,i,j-1)
            i = j
        elif j == len(s1)-1:
            reverse(s1,i,j)
            j += 1
        elif s1[j] != ' ':
            j += 1
    
    return ''.join(s1)



#// ====================测试代码====================
def Test(testName, input1, expectedResult):

    if(testName != None):
        print("%s begins: " % testName)

    input1 = ReverseSentence(input1)

    if (input1 == None and expectedResult == None) or (input1 != None and input1 == expectedResult):
        print("Passed.\n\n")
    else:
        print("Failed.\n\n")


#// 功能测试，句子中有多个单词
def Test1():

    input1 = "I am a student."
    expected = "student. a am I"

    Test("Test1", input1, expected)


#// 功能测试，句子中只有一个单词
def Test2():

    input1 = "Wonderful"
    expected = "Wonderful"

    Test("Test2", input1, expected)


#// 鲁棒性测试
def Test3():

    Test("Test3", None, None)


#// 边界值测试，测试空字符串
def Test4():

    Test("Test4", "", "")


#// 边界值测试，字符串中只有空格
def Test5():

    input1 = "   "
    expected = "   "
    Test("Test5", input1, expected)


s = "  hello world! "
r = ReverseSentence(s)
print(r,len(r),len(s))


# Test1()
# Test2()
# Test3()
# Test4()
# Test5()
