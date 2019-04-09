
def maxLength(str1,str2):
    if not str1 or not str2:
        return 0
    
    f = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]

    for i in range(0,len(str2)):
        for j in range(0,len(str1)):
            if str2[i] == str1[j]:
                f[i+1][j+1] = f[i][j]+1
            else:
                f[i+1][j+1] = max(f[i][j+1],f[i+1][j])

    pre = (0,0)
    for i in range(len(str2)):
        for j in range(len(str1)):
            if str2[i] == str1[j]:
                pass
    
    return f[len(str2)][len(str1)]



n = maxLength('1112233','112233')
print(n)