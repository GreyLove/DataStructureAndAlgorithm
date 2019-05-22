def Partition(a):
    if not a:
        return
    i = 0
    j = len(a)-1

    while i < j:
        while i < j and ord(a[j]) >= ord('A') and ord(a[j]) <= ord('Z'):
            j -= 1
        
        while i < j and ord(a[i]) >= ord('a') and ord(a[i]) <= ord('z'):
            i += 1
        
        t = a[j]
        a[j] = a[i]
        a[i] = t

a = ['D','a','F','B','c','A','z']
a = ['D','a']
a = ['d','a','F','B','A']

Partition(a)

print('---------')
print(a)