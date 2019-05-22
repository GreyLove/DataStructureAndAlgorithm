# 应用场景是手机号,10万手机号排序，先比较最后一位，然后倒数第二位。排11次就好了

def countSort(a,index):
    if not a:
        return
    c = [0 for _ in range(9)]
    for i in a:
        last = i[index]
        c[last] += 1
    
    for i in range(1,len(c)):
        c[i] += c[i-1]
    
    t = [None for _ in range(len(a))]

    for i in range(len(a)-1,-1,-1):
        last = a[i][index]
        idx = c[last] - 1
        c[last] -= 1
        t[idx] = a[i]
    for i in range(len(t)):
        a[i] = t[i]

def BaseSort(a):
    if not a:
        return
    for i in range(len(a[0])-1,-1,-1):
        countSort(a,i)

A = [[1,2,3],[2,3,1],[5,1,2],[1,0,0],[2,3,2]]

BaseSort(A)

print(A)