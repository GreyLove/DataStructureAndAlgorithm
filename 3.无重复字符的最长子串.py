#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (28.06%)
# Total Accepted:    78.7K
# Total Submissions: 280K
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 
# 示例 1:
# 
# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
# 
# 示例 2:
# 
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
# 
# 示例 3:
# 
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# 
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s) < 1:
            return 0

        dic = {}
        dic[s[0]] = 0
        maxCount = 1
        count = 1
        for i in range(1,len(s)):
            v = s[i]
            if not v in dic:
                dic[v] = i
                count += 1
            else:
                
                index = dic[v]
                d = i - index
                if d <= count:
                    count = d
                else:
                    count += 1
                dic[v] = i
                
            if count > maxCount:
                maxCount = count

        return maxCount


# s = "pwwkew"
# print(Solution().lengthOfLongestSubstring(s))
