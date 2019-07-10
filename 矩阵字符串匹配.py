# 矩阵匹配
def matrixMatch(s,p):
    if not s or not p :
        return
    
    row_s = len(s)
    col_s = len(s[0])

    row_p = len(p)
    col_p = len(p[0])

    if row_s < row_p or col_s < col_p:
        return
    p1 = my_hash(p,row_p,col_p)
    for i in range(row_s-row_p+1):
        for j in range(col_s-col_p+1):
            h1 = my_hash(s,i+row_p,j+col_p,i,j)
            if h1 == p1:
                print(i,j)
                return (i,j)


def my_hash(s,row,col,p=0,q=0):
    s1 = ''
    for i in range(p,row):
        for j in range(q,col):
            s1 += s[i][j]
    
    return hash(s1)

s = [['d','a','b','c'],
    ['e','f','a','d'],
    ['c','c','a','f'],
    ['d','e','f','c']]
p = [['a','f'],['f','c']]
matrixMatch(s,p)