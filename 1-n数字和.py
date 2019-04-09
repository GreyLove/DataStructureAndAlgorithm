
def find(n,target):
    if n < 0 or target < 0:
        return 0

    
    f = [[0 for _ in range(target+1)] for _ in range(n+1)]
    if n < 1:
        return 0
    f[0][0] = 1
    f[1][1] = 1
    f[1][0] = 1
    for i in range(2,n+1):
        for j in range(target+1):
            
            if f[i-1][j] > 0 and j+i<=target:
                f[i][j+i] += f[i-1][j]
            f[i][j] += f[i-1][j]


    return f

find(5,4)