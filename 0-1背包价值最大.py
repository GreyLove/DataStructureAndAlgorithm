def packageMax(weights,values,w):
    if not weights or not values:
        return 0
    if len(weights) != len(values):
        return 0
    n = len(weights)
    f = [[-1 for _ in range(w+1)] for _ in range(n)]

    if weights[0] > w:
        return 0

    f[0][weights[0]] = values[0]
    f[0][0] = 0
    for i in range(1,n):
        for j in range(w+1):
            if f[i-1][j] > -1:
                cw = weights[i]+j
                if cw <= w:
                    f[i][cw] = max(f[i-1][j]+values[i],f[i][cw])
                f[i][j] = max(f[i-1][j],f[i][j])

    maxValue = -1
    for i in range(w+1):
        if maxValue < f[n-1][i]:maxValue = f[n-1][i]
    
    return maxValue

    


weights = [2,2,4,6,3]
values =  [3,4,8,9,6]
w = 15

v = packageMax(weights,values,w)
print(v)