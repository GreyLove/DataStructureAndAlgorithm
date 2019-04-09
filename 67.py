# #// 面试题67：把字符串转换成整数
# #// 题目：请你写一个函数StrToInt，实现把字符串转换成整数这个功能。当然，不
# #// 能使用atoi或者其他类似的库函数。

def StrToInt(string):
    if not string or len(string) == 0:
        return "error"
    
    fisrtChar = string[0]
    
    if not (fisrtChar == '+' or fisrtChar == '-' or (ord(fisrtChar)>ord('0') and ord(fisrtChar)<ord('9'))):
        return "error"
    
    if len(string) == 1 and (fisrtChar == '+' or fisrtChar == '-'):
        return "error"

    s = 0
    for i in range(len(string)):
        if i == 0 and (string[i] == '+' or string[i] == '-'):
            continue
        else:
            if not (ord(string[i])>=ord('0') and ord(string[i])<=ord('9')):
                return "error"
            s = s*10+(ord(string[i])-ord('0'))
    
    if fisrtChar == '-':
        return -s
    
    return s



# #// ====================测试代码====================
def Test(string):

    result = StrToInt(string)
    if isinstance(result,int):
        print("str:",string ,"数字result:",result)
    else:
        print("str:",string ,"result:",result)





Test(None)

Test("")

Test("123")

Test("+123")

Test("-123")

Test("1a33")

Test("+0")

Test("-0")

#//有效的最大正整数, 0x7FFFFFFF
Test("+2147483647")    

Test("-2147483647")

Test("+2147483648")

#//有效的最小负整数, 0x80000000
Test("-2147483648")    

Test("+2147483649")

Test("-2147483649")

Test("+")

Test("-")

