def match(str1,str2):
    n = len(str1)
    m = len(str2)

    if n ==0 or m == 0:
        return False 

    if n < m:
        return False
    
    for i in range(0,n-m+1):

        if str1[i] == str2[0]:

            k = i
            j = 0

            find = True
            while j < m:
                if str1[k] != str2[j]:
                    find = False
                    break
                j += 1
                k += 1
            
            if find:return find
    

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
