def insertSort(a):
    if a == None or len(a) <= 1:
        return
    n = len(a)
    for i in range(1,n):
        if a[i] < a[i-1]:
            j = i-1
            val = a[i]
            while j >= 0:
                if val < a[j]:
                    a[j+1] = a[j]
                else:
                    break
                j -= 1
            a[j+1] = val

a = [2,3,4,1,5,4,6,1,7,1]
a = [1,2,3,4,5]
a = [5,4,3,2,1]

insertSort(a)
print(a)