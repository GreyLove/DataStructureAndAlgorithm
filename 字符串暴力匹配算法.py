# 字符串暴力匹配算法 BF算法
# 子串个数是n-m+1: n 是字符串长度，m 是模式串的长度
# 时间复杂度最差是：O(n*m)  n-m+1 * m
def BF(s,p):
    if not s or not p:
        return False
    if len(s) < len(p):
        return False
    
    for i in range(len(s)-len(p)+1):
        c = s[i]
        if c == p[0]:
            match = True
            for j in range(len(p)):
                c2 = s[i+j]
                c1 = p[j]
                if c2 != c1:
                    match = False
                    break
            if match:
                print(i)
                return i
    
    return False


s = 'aacaab'
p = 'aa'

BF(s,p)

    