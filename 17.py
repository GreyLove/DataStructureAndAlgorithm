# // 面试题17：打印1到最大的n位数
# // 题目：输入数字n，按顺序打印出从1最大的n位十进制数。比如输入3，则
# // 打印出1、2、3一直到最大的3位数即999。

def PrintNumber(n):
    if n == 0:
        return
    t = [0 for _ in range(n+1)]
    while t[0] != 1:
        result = digits(t)
        if t[0] == 1:
            break
        print(result)

def digits(t):
    
    j = len(t)-1
    t[j] += 1

    while j > 0:
        if t[j] >= 10:
            t[j-1] += 1
            t[j] -= 10
        else:
            break
        j -= 1
    l = []
    for i in range(len(t)):
        if i == 0 and t[i] == 0:
            continue
        else:
            l.append(str(t[i]))
        
    return ''.join(l)

# def intToStr(t)




PrintNumber(3)
