#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (31.82%)
# Total Accepted:    51.2K
# Total Submissions: 160.6K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
# 
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
# 
# 说明:
# 
# 所有输入只包含小写字母 a-z 。
# 
#
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs or len(strs) == 0:
            return ""
        tmp = [0 for _ in range(26)]
        minStr = strs[0]
        for s in strs:
            if len(minStr) >= len(s):
                minStr = s
        
        
        i = 0
        ss = ''
        while i < len(minStr):
            for s in strs:
                tmp[ord(s[i])-ord('a')] += 1
            if tmp[ord(s[i])-ord('a')] == len(strs):
                ss += s[i]
                tmp[ord(s[i])-ord('a')] = 0
            else:
                break
            i += 1

        return ss

# strs = ["flower","flow","floght"]
# strs = ["dog","racecar","car"]
# n = Solution().longestCommonPrefix(strs)
# print(n)

        


