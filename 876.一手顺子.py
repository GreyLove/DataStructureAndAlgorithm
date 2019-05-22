#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 一手顺子
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        if head == None or head.next == None:
            return head
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow        

