# // 面试题57（一）：和为s的两个数字
# // 题目：输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们
# // 的和正好是s。如果有多对数字的和等于s，输出任意一对即可。


def FindNumbersWithSum(a,s):
    if not a or len(a) == 0:
        return -1,-1
    
    i = 0
    j = len(a)-1

    s_add = 0
    while i < j:
        s_add = a[i]+a[j]
        if s_add == s:
            return a[i],a[j]
        elif s_add > s:
            j -= 1
        elif s_add < s:
            i += 1
    
    return -1,-1







data = [1, 2, 4, 7, 11, 15] #true
s = 15

data = [1, 2, 4, 7, 11, 16] #true
s = 17

data = [1, 2, 4, 7, 11, 16] #false
s = 10

a,b = FindNumbersWithSum(data,s)
print(a,b)
