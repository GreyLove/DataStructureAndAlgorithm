def find(a,target):
    if not a:
        return
    
    i = 0
    j = len(a)-1
    while i <= j:
        m = (i+j)>>1
        if  a[m] <= target:
            if m == len(a) - 1 or a[m+1] > target:
                return m
            else:
                i = m+1
        elif a[m] > target:
            j = m-1

    

      

a = [2,2,5,5,5,5,6,6,6,7,7]
a = [2,2,5,7,7,7,7,9,10]

# a = [7,7,7,7,7]
target = 4
idx = find(a,target)
print(idx,'-----',a[idx])