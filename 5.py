# // 面试题5：替换空格
# // 题目：请实现一个函数，把字符串中的每个空格替换成"%20"。例如输入“We are happy.”，
# // 则输出“We%20are%20happy.”。


def ReplaceBlank(s):
    if not str or len(s) == 0:
        return
    
    blank = 0

    for r in s:
        if r == ' ':
            blank += 1
    
    if blank == 0:
        return s

    newStrList = [None for _ in range(blank*2+len(s))]

    i = len(s)-1
    j = len(newStrList)-1

    while i >= 0:
        if s[i] == ' ':
            newStrList[j] = '0'
            newStrList[j-1] = '2'
            newStrList[j-2] = '%'
            j = j-2
        else:
            newStrList[j] = s[i]
        
        i -= 1
        j -= 1
    
    return ''.join(newStrList)




def Test(str):
    url = ReplaceBlank(str)
    url1 = str.replace(' ','%20')
    if url == url1:
        print('**********success********')
    else:
        print('**********failtrue********')
    print(url,len(url),'----',url1,len(url1))

Test('we are happy.')

Test(' we are happy.')

Test(' we are happy. ')

Test(' ')

Test('111')
