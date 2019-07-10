def kmp(a,b):
    next = getNexts(b)
    j = 0
    n = len(a)
    m = len(b)
    for i in range(n):
        while j>0 and a[i]!=b[j]: #精华的部分，很巧妙的模式串进行了移动。
            j = next[j-1]+1 #比较前缀之后，+1是为了接着比较后一位的，也是比较的前缀，很巧妙
        
        if a[i] == b[j]:
            j += 1
        
        if j == m:
            return i-m+1
    
    return -1

# 找到前缀，和 后缀 最长的串的方法
def getNexts(b):

    m = len(b)
    next = [-1 for _ in range(len(b))]

    # next[0] = -1  k = -1 ,-1 代表没有找到
    k = -1

    for i in range(1,m):

        while k != -1 and b[k+1] != b[i]: 
            #精华部分，如果条件满足，说明当前比较的字符不匹配，k是上一个可匹配的最大长度前缀末尾字符的下标， 
            # 那么i-1 最长的前缀不匹配，需要找到次长的那个可以匹配的，然后比较字符是否相同，直到-1或找到
            # 次长怎么找？  最长 h  字符串 中的 最长匹配子串，所以是k = next[k]，
            # 一定要理解前缀的最大可匹配子串，就是相当于最长 h  字符串 中的 次长匹配子串
            k = next[k] # 前缀的首尾，相当于前后缀的首尾，只有前缀首尾一致，才能是次长子串，所以k = next[k]。前缀的next[k] 就是 最长匹配子串的次长
            # 最重要就是最长匹配子串找次长子串，次长子串就是找[0，y]的最长串,y 是最长子串的下标
            # k = next[k] 找到最长子串的次长子串。
        if b[k+1] == b[i]:
            k+=1
        
        next[i] = k
    
    # print(next)
    return next




# 我们假设 b[0, i] 的最长可匹配后缀子串是 b[r, i],那么b[0,i-1] 
# 的可以匹配字符是b[r,i-1],但那是不一定是最长的可匹配后缀 
# 例如：aacaaa -> aa, aacaa -> a 其实是（aacaa -> aa）

# 主要思路：
# j 在模式串b 上移动，i 在主串a移动。
# 当遇到不同子串的时候去找b的前缀匹配 a的后缀，然后j在b上移动
# 每次复位j的位置，j在b上进退，i在a一直向后移动

a = "ababaeababacd"
b = "ababacd"


print(kmp(a,b))
getNexts(b)