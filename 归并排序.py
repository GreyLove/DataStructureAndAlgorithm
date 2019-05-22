
def mergeSort(a):
    if a == None or len(a) < 2:
        return a
    return mergeCore(a,0,len(a)-1)

def mergeCore(a,i,j):
    if i >= j:
        return [a[i]]
    m = (i+j)>>1
    l = mergeCore(a,i,m)
    r = mergeCore(a,m+1,j)
    return merge(l,r)

def merge(a,b):
    if a == None or b == None:
        return []
    i = 0
    j = 0
    t = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            t.append(a[i])
            i += 1
        else:
            t.append(b[j])
            j += 1
    
    while i < len(a):
        t.append(a[i])
        i += 1

    while j < len(b):
        t.append(b[j])
        j += 1
    
    return t


a = [4,2,5,1,6]
a = [1,2,3,4,5]
a = [1,2]
a = [2,1]
# a = [2]

nw = mergeSort(a)

print(nw)