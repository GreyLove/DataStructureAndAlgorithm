# // 面试题56（一）：数组中只出现一次的两个数字
# // 题目：一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序
# // 找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

def FindNumsAppearOnce(data):
    if not data or len(data) == 0:
        return -1,-1
    
    s = 0
    for d in data:
        s ^= d

    k = 0
    for i in range(64):
        if (s & 1<<i) > 0:
            k = i
            break
    
    l1 = []
    l2 = []
    for d in data:
        if d & 1<<k:
            l1.append(d)
        else:
            l2.append(d)

    s1 = 0
    s2 = 0

    for d in l1:
        s1 ^= d
    
    for d in l2:
        s2 ^= d

    return s1,s2





n = [1,1,2,2,3,5]
n = [2, 4, 3, 6, 3, 2, 5, 5 ]
n = [4, 6]
n = [4, 6, 1, 1, 1, 1 ]
a,b = FindNumsAppearOnce(n)
print(a,b)
