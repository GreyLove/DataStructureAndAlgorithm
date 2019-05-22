# 6、1到N分成两个集合，两个和相等，问有几种分法

def towSetOfCount(n):
    if n <= 1:
        return 0
    sum = (n**2+n)>>1
    if sum & 1:
        return 0
    half = sum>>1
    return core(n,half)>>1

def core(i,sum):
    if i < 0 or sum<0:
        return 0
    if i == 0 and sum == 0:
        return 1
    if i == 0 and sum > 0:
        return 0
    if i > sum:
        return core(i-1,sum)
    else:
        return core(i-1,sum)+core(i-1,sum-i)


def towSetOfCount1(n):
    if n <= 1:
        return 0
    sum = (n**2+n)>>1
    if sum & 1:
        return 0
    half = sum>>1

    c = [[0 for _ in range(half+1)] for _ in range(n+1)]
    c[0][0] = 1

    for i in range(1,n+1):
        for j in range(0,half+1):
            if i > half:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = c[i-1][j] + c[i-1][j-i]
    
    return c[n][half]>>1

k = 15
count = towSetOfCount(k)
print(count)

count = towSetOfCount1(k)
print(count)
            
    

