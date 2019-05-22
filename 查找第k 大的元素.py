
def postive(a,i,j):
    if i >= j:
        return i
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

def findK(a,k):
    if k > len(a) or k <= 0:
        return -1
    p = len(a)-k
    i = 0
    j = len(a)-1
    m = postive(a,i,j)
    while m != p:
        if m < p:
            i = m + 1
        elif m > p:
            j = m - 1
        m = postive(a,i,j)
    return a[m]

a = [4,2,5,1,6]

n = findK(a,6)

print(n)