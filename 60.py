# // 面试题60：n个骰子的点数
# // 题目：把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s
# // 的所有可能的值出现的概率。

kkk = 6

def PrintProbability_Solution1(n):
    if n < 1:
        return
    
    tmp = [0 for _ in range(n*kkk+1)]
    PrintProbability_Solution1Core(n,tmp,0)
    print(tmp[n:])

def PrintProbability_Solution1Core(n,tmp,k):
    if n == 1:
        for i in range(1,kkk+1):
            tmp[i+k] += 1
        return

    for i in range(1,kkk+1):
        PrintProbability_Solution1Core(n-1,tmp,i+k)
    
        

def PrintProbability_Solution2(n):
    if n < 1:
        return
    f1 = [0 for _ in range(kkk*n+1)]
    f2 = [0 for _ in range(kkk*n+1)]
    f = [f1,f2]

    flag = 0

    for i in range(1,kkk+1):
        f1[i] = 1
    
    for i in range(2,n+1):
        for x in range(0,i):
            f[1-flag][x] = 0
        for j in range(i,kkk*i+1):
            f[1-flag][j] = 0
            p = 1
            while p < j and p <= kkk:
                f[1-flag][j] += f[flag][j-p]
                p += 1
        flag = 1-flag

    print(f[flag][n:])
    return f[1-flag]
             


k = 9
PrintProbability_Solution1(k)
PrintProbability_Solution2(k)
