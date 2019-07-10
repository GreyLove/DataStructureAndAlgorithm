# 字符算匹配，主要思想是 计算每个子串的hash 值，然后和 模式串的 hash 值做比较。
# 子串个数是n-m+1: n 是字符串长度，m 是模式串的长度
# 综合时间复杂度是O(n),涉及到字符串的hash 算法的问题
# 这个主要是思想上的
# 只有小写的26 个字母
def RK(s,p):
    if not s or not p:
        return False
    if len(s) < len(p):
        return False
    n = len(s)
    m = len(p)
    hashList = []
    s1 = 0

    for j in range(m):
        s1 += translate(s[j])*power26(m-j-1)

    hashList.append(s1)
    for i in range(1,n-m+1):
        s1 -= translate(s[i-1])*power26(m-1)
        s1 *= power26(1)
        s1 += translate(s[i+m-1])
        hashList.append(s1)

    hash_p = 0
    for j in range(m):
        hash_p += translate(p[j])*power26(m-j-1)
    

    for i in range(len(hashList)):
        if hashList[i] == hash_p:
            print(i)
            return i
        

def power26(n):
    return 26**n

def translate(char):
    return ord(char)-ord('a')+1


s = 'aacaab'
p = 'b'

RK(s,p)