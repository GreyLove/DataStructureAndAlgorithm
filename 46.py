# // 面试题46：把数字翻译成字符串
# // 题目：给定一个数字，我们按照如下规则把它翻译为字符串：0翻译成"a"，1翻
# // 译成"b"，……，11翻译成"l"，……，25翻译成"z"。一个数字可能有多个翻译。例
# // 如12258有5种不同的翻译，它们分别是"bccfi"、"bwfi"、"bczi"、"mcfi"和
# // "mzi"。请编程实现一个函数用来计算一个数字有多少种不同的翻译方法。

def findCount1(number):
    if number < 0:
        return 0


    nList = list(str(number))
    count = [0]
    findCount1Core(nList,0,[],count)
    return count[0]

def findCount1Core(nList,begin,tmp,count):
    if begin >= len(nList):
        count[0] += 1
        print(tmp)
        return 0
    c = translation(nList[begin])
    tmp.append(c)
    findCount1Core(nList,begin+1,tmp,count)
    tmp.pop()
    if begin < len(nList)-1:
        s = int(nList[begin] + nList[begin+1])
        if s>=10 and s <= 25:
            c = translation(nList[begin])
            tmp.append(c)
            findCount1Core(nList,begin+2,tmp,count)
            tmp.pop()

     

    

    
def translation(str1):
    n = int(str1)
    if n <= 25:
        c = chr(97+n)
        return c
    else:
        return ""

    

#动态规划
def findCount(number):
    if number < 0:
        return 0

    nList = list(str(number))
    
    f = [0 for _ in range(len(nList)+1)]
    k = len(nList)
    f[k] = 1
    f[k-1] = 1
    i = k-2

    while i >= 0:
        s = int(nList[i] + nList[i+1])
        if s>=10 and s <= 25:
            f[i] = f[i+1]+f[i+2]
        else:
            f[i] = f[i+1]
        i -= 1
        
    return f[0]




# // ====================测试代码====================
def Test(testName,number,expected):

    if(findCount1(number) == expected):
        print(testName," passed.")
    else:
        print(testName," FAILED.")

def Test1():

    number = 12258
    expected = 5
    Test("Test1", number, expected)


def Test2():

    number = 10
    expected = 2
    Test("Test2", number, expected)


def Test3():

    number = 125
    expected = 3
    Test("Test3", number, expected)


def Test4():

    number = 126
    expected = 2
    Test("Test4", number, expected)


def Test5():

    number = 426
    expected = 1
    Test("Test5", number, expected)


def Test6():

    number = 100
    expected = 2
    Test("Test6", number, expected)


def Test7():

    number = 101
    expected = 2
    Test("Test7", number, expected)


def Test8():

    number = 12258
    expected = 5
    Test("Test8", number, expected)


def Test9():

    number = -100
    expected = 0
    Test("Test9", number, expected)


Test1()
Test2()
Test3()
Test4()
Test5()
Test6()
Test7()
Test8()
Test9()
