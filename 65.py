# // 面试题65：不用加减乘除做加法
# // 题目：写一个函数，求两个整数之和，要求在函数体内不得使用＋、－、×、÷
# // 四则运算符号。

def sum(a,b):
    s = 0
    jinwei = 0
    for i in range(64):
        k = 1<<i
        one = 0
        if a & k > 0 and b & k > 0:
            if jinwei != 0:
                one = 1
            jinwei = 1
        elif a & k == 0 and b & k == 0:
            if jinwei == 1:
                one = 1
                jinwei = 0
        else:
            if jinwei == 0:
                one = 1
        
        if one==1:
            s |= k
        
    return s

# 更简单的算法，利用^ 获取1的位，利用&获取进位.pyhton 没办法用这个，因为-1 1位无限大
def sum1(a,b):
    
    s = 0
    c = 0
    s = a^b
    c = (a&b)<<1
    a = s
    b = c
    while b != 0:
        s = a^b
        c = (a&b)<<1
        a = s
        b = c
    
    return a

s = sum(-3,-3) 
# s1 = sum1(-3,3)
print(s)   

