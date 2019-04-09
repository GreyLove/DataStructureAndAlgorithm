# // 面试题50（一）：字符串中第一个只出现一次的字符
# // 题目：在字符串中找出第一个只出现一次的字符。如输入"abaccdeff"，则输出
# // 'b'。

def FirstNotRepeatingChar(s:str)->str:
    if not s or len(s) == 0:
        return ''
    
    m = {}

    for i in range(len(s)):
        if s[i] in m.keys():
            m[s[i]] += 1
        else:
            m[s[i]] = 1
    
    for i in s:
        if m[i] == 1:
            return i
    
    return ''


# // ====================测试代码====================
def Test(pString,expected):

    if(FirstNotRepeatingChar(pString) == expected):
        print("Test passed.\n")
    else:
        print("Test failed.\n")


# // 常规输入测试，存在只出现一次的字符
Test("google", 'l')

# // 常规输入测试，不存在只出现一次的字符
Test("aabccdbd", '')

# // 常规输入测试，所有字符都只出现一次
Test("abcdefg", 'a')

# // 鲁棒性测试，输入nullptr
Test(None, '')