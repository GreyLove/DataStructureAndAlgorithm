# 比如 5，8，5，2，9 这样一组数据，不稳定排序， 5 和 2 交换，然后第一个5 被放在了后面
def selectSort(a):
    if a == None or len(a) <= 1:
        return
    n = len(a)
    for i in range(n-1):
        m = i
        for j in range(i+1,n):
            if a[j] < a[m]:
                m = j
        t = a[i]
        a[i] = a[m]
        a[m] = t

a = [2,3,4,1,5,4,6,1,7,1]
# a = [1,2,3,4,5]

selectSort(a)
print(a)