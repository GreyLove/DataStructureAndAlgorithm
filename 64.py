# / 面试题64：求1+2+…+n
# // 题目：求1+2+…+n，要求不能使用乘除法、for、while、if、else、switch、case
# // 等关键字及条件判断语句（A?B:C）。

def sum(n):
    return (1+n)*(n/2)


n = sum(100)
print(n)
