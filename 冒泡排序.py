def bubbleSort(a):
    if a == None or len(a) <= 1:
        return
    
    for i in range(len(a)-1):
        flag = False
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                t = a[j]
                a[j] = a[j+1]
                a[j+1] = t
                flag = True
        if not flag:
            return

a = [2,3,4,1,5,7,2,4,1,6]
# a = [1,2,3,4,5]
bubbleSort(a)
print(a)