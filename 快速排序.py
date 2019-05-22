def quickSort(a):
    if a == None or len(a) < 2:return a
    quickSortCore(a,0,len(a)-1)

def mid(a,i,j):
    mid = (i+j)>>1

    if a[i] > a[j]:
        t = a[i]
        a[i] = a[j]
        a[j] = t
    
    if a[mid] > a[j]:
        t = a[mid]
        a[mid] = a[j]
        a[j] = t
    
    if a[mid] < a[i]:
        t = a[mid]
        a[mid] = a[i]
        a[i] = t

    t = a[mid]
    a[mid] = a[i]
    a[i] = t

def postive(a,i,j):
    if i >= j:
        return
    
    mid(a,i,j)

    sentry = a[i]

    while i < j:
        while i < j and a[j] >= sentry:
            j -= 1
        a[i] = a[j]

        while i < j and a[i] <= sentry:
            i += 1
        a[j] = a[i]

    a[j] = sentry
    return j 

def quickSortCore(a,i,j):
    if i < j:
        m = postive(a,i,j)
        quickSortCore(a,i,m-1)
        quickSortCore(a,m+1,j)


a = [4,2,5,1,6]
a = [4,4,5,5,2,2]
a = [11,11,11,22,22,22]

# a = [1,2,3,4,5]
# a = [1,2]
# a = [2,1]
# a = [2]

quickSort(a)

print(a)