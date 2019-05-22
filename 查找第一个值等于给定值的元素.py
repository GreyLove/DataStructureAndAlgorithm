# 默认是从小到大排序的
# 我的思路是先找到相等的，然后前移
def find(a,target):
    if not a:
        return
    
    i = 0
    j = len(a)-1
    while i <= j:
        m = (i+j)>>1
        if  a[m] == target:
            if m == 0 or a[m-1] != a[m]:
                return m
            else:
                j = m-1
        elif a[m] > target:
            j = m-1
        elif a[m] < target:
            i = m+1
    
    
    return -1

a = [2,2,5,5,5,5,6,6,6,7,7]
# a = [7,7,7,7,7]
target = 4
idx = find(a,target)
print(idx)