# // 面试题38：字符串的排列
# // 题目：输入一个字符串，打印出该字符串中字符的所有排列。例如输入字符串abc，
# // 则打印出由字符a、b、c所能排列出来的所有字符串abc、acb、bac、bca、cab和cba。


def Permutation(s):
    if len(s) == 0:
        return
    PermutationCore(list(s),0)
    
# 核心思想就是第一个字符和后面的交换
def PermutationCore(s,begin):
    if begin >= len(s):
        print(''.join(s))
        return

    for i in range(begin,len(s)):

        tmp = s[i]
        s[i] = s[begin]
        s[begin] = tmp

        PermutationCore(s,begin+1)

        tmp = s[i]
        s[i] = s[begin]
        s[begin] = tmp




string = 'abc'
begin = 0
Permutation(string)
