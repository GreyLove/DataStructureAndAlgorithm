def match(str1,str2):
    n = len(str1)
    m = len(str2)

    if n ==0 or m == 0:
        return False 

    if n < m:
        return False

    def digit(ch):
        return (ord(ch)-ord('a'))
    
    def hash(s1):
        k = len(s1)-1
        s = 0
        i = 0
        while k>=0:
            s += digit(s1[i])*(26**k)
            k -= 1
            i+=1
        return s
    
    tmp = []
    s = hash(str1[0:m])
    tmp.append(s)
    for i in range(1,n-m+1):
        s = (s - digit(str1[i-1])*(26**(m-1)))*26+digit(str1[i+m-1])
        tmp.append(s)
    
    s1 = hash(str2)

    for t in tmp:
        if t == s1:
            return True
    
    return False




def Test():
    print(match('hello','llo'),True)
    print(match('hello','llo1'),False)
    print(match('hello',''),False)
    print(match('','llo1'),False)
    print(match('a','a'),True)
    print(match('a','ab'),False)
    print(match('helloworld','hello'),True)
    print(match('helloworld','world'),True)

Test()