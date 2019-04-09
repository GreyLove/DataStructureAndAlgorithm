


class PatternMap(object):
    def __init__(self):
        self.h = [-1 for _ in range(256)]
    
    def put(self,ch,i):
        self.h[ord(ch)] = i

    def get(self,ch):
        return self.h[ord(ch)]


def match(str1,str2):
    n = len(str1)
    m = len(str2)

    if n ==0 or m == 0:
        return False 

    if n < m:
        return False
    
    h = PatternMap()

    for i in range(m):
        h.put(str2[i],i)

        # 好后缀
    # 预处理一下

    suffix = [-1 for _ in range(n)]
    prefix = [False for _ in range(n)]
    for i in range(m-1):
        j = i
        k = 0

        while j>= 0 and str2[j] == str2[m-1-k]:
            j -= 1
            k += 1
            suffix[k] = j+1
        
        if j == -1:
            prefix[k] = True

    
    i = 0

    #坏字符
    while i <= n-m+1:
        k1 = i+m-1
        k2 = m-1
        move = 0
        while k2>=0:
            if str1[k1] != str2[k2]:
                si = k2
                xi = h.get(str1[k1])
                move = si-xi
                i += move
                break
            k2-=1
            k1-=1

        if k2 == -1:
            return True

        

    print("")
        
        
match('abcde','bcd')
    
            

            
                 

        


    