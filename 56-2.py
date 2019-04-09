# // 面试题56（二）：数组中唯一只出现一次的数字
# // 题目：在一个数组中除了一个数字只出现一次之外，其他数字都出现了三次。请
# // 找出那个吃出现一次的数字。

def FindNumberAppearingOnce(n):
    if not n or len(n) == 0:
        return -1
    
    tmp = [0 for _ in range(64)]

    for d in n:
        for i in range(64):
            if d&(1<<i):
                tmp[i] += 1
    
    for i in range(64):
        tmp[i] = tmp[i]%3
    
    s = 0
    for i in range(64):
        s += tmp[i]*(2**i)
    
    return s




# n = [1, 1, 2, 2, 2, 1, 3]
# n = [4, 3, 3, 2, 2, 2, 3]
# n = [4, 4, 1, 1, 1, 7, 4]
# n = [-10, 214, 214, 214 ] #python int 无限大
# n = [-209, 3467, -209, -209]
# n = [-1024, -1024, -1024, -1023]
# n = [0, 3467, 0, 0, 0, 0, 0, 0 ]
s = FindNumberAppearingOnce(n)
print(s)
