# 桶排序的特殊方法，适用于范围小的排序
# 比如范围0-5,可以创建5个桶，然后记录数据在每个桶的分布，然后做一个<=的一个操作，现在C数据存放的就是<= 包含本身的数据个数，然后逆序遍历A,没遍历一个数，就在C里对应-1
# A[8] = [2，5，3，0，2，3，0，3]

def countSort(a):
    if not a:
        return
    c = [0 for _ in range(9)]
    for i in a:
        c[i] += 1
    
    for i in range(1,len(c)):
        c[i] += c[i-1]
    
    t = [None for _ in range(len(a))]

    for i in range(len(a)-1,-1,-1):
        idx = c[a[i]] - 1
        c[a[i]] -= 1
        t[idx] = a[i]
    for i in range(len(t)):
        a[i] = t[i]

a = [2,5,3,0,2,3,0,3]
countSort(a)
print(a)