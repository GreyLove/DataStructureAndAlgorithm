
def maxWeight(weights,w):
    if len(weights) == 0 or w < 0:
        return 0

    n = len(weights)
    f = [[0 for _ in range(w+1)] for _ in range(n)]
    

    if weights[0] > w:
        return 0

    f[0][weights[0]] = 1
    f[0][0] = 1

    for i in range(1,n):
        ww = weights[i]
        for j in range(w+1):
            if f[i-1][j] == 1:
                if ww+j<=w:
                    f[i][ww+j] = 1
                f[i][j] = 1
    i = w
    while i >= 0:
        if f[n-1][i] == True: return i
        i -= 1
    return f
    


weights = [2,2,4,6,3]
w = 19
print(maxWeight(weights,w))