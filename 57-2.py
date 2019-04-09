# // 面试题57（二）：为s的连续正数序列
# // 题目：输入一个正数s，打印出所有和为s的连续正数序列（至少含有两个数）。
# // 例如输入15，由于1+2+3+4+5=4+5+6=7+8=15，所以结果打印出3个连续序列1～5、
# // 4～6和7～8。

def FindContinuousSequence(k):
    print("begin-----%d",k)
    if k < 3:
        return
    
    n = (k+1)>>1

    i = 1
    j = 2
    s = i + j
    while i < j and j <= n:
        if s == k:
            print(i,'~',j)
            j += 1
            s += j
            s -= i
            i += 1
        elif s>k:
            s -= i
            i += 1                
        elif s<k:
            j += 1
            s += j



# FindContinuousSequence(1)
# FindContinuousSequence(3)
# FindContinuousSequence(4)
# FindContinuousSequence(9)
# FindContinuousSequence(15)
FindContinuousSequence(1001)
