#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] Backspace String Compare
#
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        statck = []
        for i in S:
            if i == '#':
                if len(statck):statck.pop()
            else:
                statck.append(i)
        S = ''.join(statck)
        statck.clear()
        for i in T:
            if i == '#':
                if len(statck):statck.pop()
            else:
                statck.append(i)
        T = ''.join(statck)

        if S == T:
            return True
        else:
            return False

