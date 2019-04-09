
def findMoney(i,m,n):
    if i < 0 or m<0:
        return 0
    
    if m == 5:
        return 1
    elif m == 3:
        return 1
    elif m == 1:
        return 1
   
    minNum = findMoney(i-1,m-n[0],n)
    for k in range(1,len(n)):
        if  m-n[k]>0 and minNum > findMoney(i-1,m-n[k],n):
            minNum = findMoney(i-1,m-n[k],n)
    
    return minNum+1


def findMoney1(m,n):
    if m<1:
        return 0

    for i in range(len(n)-1,-1,-1):
        if m == n[i]:return 1
    
    
    f = [[0 for _ in range(m+1)] for _ in range(m)]
    
    for i in range(len(n)):
        if n[i] <= m:f[0][n[i]] = 1
        
    for i in range(1,m):
        for j in range(m):
            if f[i-1][j] > 0:
                for k in range(len(n)):
                    if n[k]+j <= m:
                        if f[i][j+n[k]]>0:
                            f[i][j+n[k]] = min(f[i][j+n[k]],f[i-1][j]+1)
                        else:
                            f[i][j+n[k]] += f[i-1][j]+1
                f[i][j] = f[i-1][j]

    return f[m-1][m]
                
            

t = 39

n1 = findMoney1(t,[1,3,5])
print(n1)

n = findMoney(t,t,[1,3,5])
print(n)



    
