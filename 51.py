# // 面试题51：数组中的逆序对
# // 题目：在数组中的两个数字如果前面一个数字大于后面的数字，则这两个数字组
# // 成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

def InversePairs(data):
    if not data or len(data) == 0:
        return 0
    
    i = 0
    j = len(data)-1

    count = [0]
    InversePairsCore(data,i,j,count)
    return count[0]

    
    
def InversePairsCore(data,i,j,count:list):
    if i == j:
        return [data[i]]
    if i < j:
        m = (i+j)>>1
        l = InversePairsCore(data,i,m,count)
        r = InversePairsCore(data,m+1,j,count)
        tmp = mergeList(l,r,count)
        return tmp
        

def mergeList(a,b,count:list):
    i = len(a)-1
    j = len(b)-1
    tmp = [None for _ in range(len(a)+len(b))]
    k = len(tmp)-1
    while i >= 0 and j >= 0:
        v = a[i]
        if a[i] > b[j]:
            count[0] += j+1
            i -= 1
        else:
            j -= 1
            v = b[j]
        
        tmp[k] = v
        k -= 1
    
    while i >= 0:
        tmp[k] = a[i]
        k -= 1
        i -= 1

    while j >= 0:
        tmp[k] = b[j]
        k -= 1
        j -= 1
    
    return tmp
        
    
    




a = [7,5,6,4] #5
# a = [1, 2, 3, 4, 7, 6, 5] #3
# a = [6, 5, 4, 3, 2, 1] # 15
# a = [1, 2, 3, 4, 5, 6] #0
# a = [1, 2] #0
# a = [2, 1] #1
# a = [1, 2, 1, 2, 1] #3

n = InversePairs(a)
print(n)
