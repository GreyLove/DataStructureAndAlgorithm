#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#
# https://leetcode-cn.com/problems/reverse-words-in-a-string/description/
#
# algorithms
# Medium (19.40%)
# Total Accepted:    6.1K
# Total Submissions: 31.1K
# Testcase Example:  '"the sky is blue"'
#
# 给定一个字符串，逐个翻转字符串中的每个单词。
# 
# 
# 
# 示例 1：
# 
# 输入: "the sky is blue"
# 输出: "blue is sky the"
# 
# 
# 示例 2：
# 
# 输入: "  hello world!  "
# 输出: "world! hello"
# 解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
# 
# 
# 示例 3：
# 
# 输入: "a good   example"
# 输出: "example good a"
# 解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
# 
# 
# 
# 
# 说明：
# 
# 
# 无空格字符构成一个单词。
# 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
# 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
# 
# 
# 
# 
# 进阶：
# 
# 请选用 C 语言的用户尝试使用 O(1) 额外空间复杂度的原地解法。
# 
#
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s or len(s) == 0:
            return s
        s2 = list(s)
        def reverse(a,i,j):
            while i < j:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
                i += 1
                j -= 1

        i = 0
        while i < len(s2):
            if s2[i] == ' ':
                i += 1
            else:
                break

        j = len(s2)-1
        while j >= 0:
            if s2[j] == ' ':
                j -= 1
            else:
                break

        s3 = s2[i:j+1]

        s4 = []
        i = 0
        while i < len(s3):
            if s3[i] == ' ':
                s4.append(s3[i])
                while i < len(s3) and s3[i] == ' ':
                    i += 1
            else:
                s4.append(s3[i])
                i += 1
            

        s1 = s4
        
        reverse(s1,0,len(s1)-1)

        i = 0
        j = 0
        while j < len(s1):
            if s1[i] == ' ' and s1[j] == ' ':
                i += 1
                j += 1
            elif s1[j] == ' ':
                reverse(s1,i,j-1)
                i = j
            elif j == len(s1)-1:
                reverse(s1,i,j)
                j += 1
            elif s1[j] != ' ':
                j += 1
    
        return ''.join(s1)

s = " the sky  is blue "
s1 = Solution().reverseWords(s)
print(s1)
