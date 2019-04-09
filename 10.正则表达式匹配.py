#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
# https://leetcode-cn.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (21.11%)
# Total Accepted:    9.7K
# Total Submissions: 46.1K
# Testcase Example:  '"aa"\n"a"'
#
# 给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。
# 
# '.' 匹配任意单个字符。
# '*' 匹配零个或多个前面的元素。
# 
# 
# 匹配应该覆盖整个字符串 (s) ，而不是部分字符串。
# 
# 说明:
# 
# 
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
# 
# 
# 示例 1:
# 
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 
# 
# 示例 2:
# 
# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: '*' 代表可匹配零个或多个前面的元素, 即可以匹配 'a' 。因此, 重复 'a' 一次, 字符串可变为 "aa"。
# 
# 
# 示例 3:
# 
# 输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个('*')任意字符('.')。
# 
# 
# 示例 4:
# 
# 输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 'c' 可以不被重复, 'a' 可以被重复一次。因此可以匹配字符串 "aab"。
# 
# 
# 示例 5:
# 
# 输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false
# 
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == None or p == None:
            return False
        if len(s) == 0 and len(p) == 0:
            return True
        return self.isMatchCore(s,p,0,0)
        
    def isMatchCore(self,s,p,i,j):
        if i == len(s) and j == len(p):
            return True

        if i != len(s) and j == len(p):
            return False

        if j+1<len(p) and p[j+1] == '*':
            if i < len(s) and j < len(p) and ( s[i] == p[j] or p[j] == '.'):
                return self.isMatchCore(s,p,i,j+2) or \
                    self.isMatchCore(s,p,i+1,j) or \
                        self.isMatchCore(s,p,i+1,j+2)
            else:
                return self.isMatchCore(s,p,i,j+2)
        
        if i < len(s) and j < len(p) and (s[i] == p[j] or p[j] == '.'):
            return self.isMatchCore(s,p,i+1,j+1)

        return False

s = 'aaaaaaaaaab'
p = 'a*a*a*a*a*a*a*c'

n = Solution().isMatch(s,p)
print(n)


# // ====================测试代码====================
# def Test(testName, string, pattern, expected):
#     if(testName != None):
#         print("%s begins: "% (testName))

#     if( Solution().isMatch(string, pattern) == expected):
#         print("Passed.")
#     else:
#         print("FAILED.")

# Test("Test01", "", "", True)
# Test("Test02", "", ".*", True)
# Test("Test03", "", ".", False)
# Test("Test04", "", "c*", True)
# Test("Test05", "a", ".*", True)
# Test("Test06", "a", "a.", False)
# Test("Test07", "a", "", False)
# Test("Test08", "a", ".", True)
# Test("Test09", "a", "ab*", True)
# Test("Test10", "a", "ab*a", False)
# Test("Test11", "aa", "aa", True)
# Test("Test12", "aa", "a*", True)
# Test("Test13", "aa", ".*", True)
# Test("Test14", "aa", ".", False)
# Test("Test15", "ab", ".*", True)
# Test("Test16", "ab", ".*", True)
# Test("Test17", "aaa", "aa*", True)
# Test("Test18", "aaa", "aa.a", False)
# Test("Test19", "aaa", "a.a", True)
# Test("Test20", "aaa", ".a", False)
# Test("Test21", "aaa", "a*a", True)
# Test("Test22", "aaa", "ab*a", False)
# Test("Test23", "aaa", "ab*ac*a", True)
# Test("Test24", "aaa", "ab*a*c*a", True)
# Test("Test25", "aaa", ".*", True)
# Test("Test26", "aab", "c*a*b", True)
# Test("Test27", "aaca", "ab*a*c*a", True)
# Test("Test28", "aaba", "ab*a*c*a", False)
# Test("Test29", "bbbba", ".*a*a", True)
# Test("Test30", "bcbbabab", ".*a*a", False)

