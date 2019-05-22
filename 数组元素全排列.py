
def all(a):
    if not a:
        return
    allCore(a,0)

def allCore(a,begin):
    if begin >= len(a):
        print(a)


    for i in range(begin,len(a)):
        t = a[begin]
        a[begin] = a[i]
        a[i] = t

        allCore(a,begin+1)

        t = a[begin]
        a[begin] = a[i]
        a[i] = t

a = ['a','b','c']
all(a)



# n + n*(n-1) + n*(n-1)*(n-2)  + ... + n*(n-1)*(n-2)...*2*1
