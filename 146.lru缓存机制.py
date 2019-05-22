#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#
# https://leetcode-cn.com/problems/lru-cache/description/
#
# algorithms
# Hard (38.42%)
# Total Accepted:    5.5K
# Total Submissions: 14.1K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
# 
# 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) -
# 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。
# 
# 进阶:
# 
# 你是否可以在 O(1) 时间复杂度内完成这两种操作？
# 
# 示例:
# 
# LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得密钥 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得密钥 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
# 
# 
#

class Node:

    def __init__(self,val,key):
        self.val = val
        self.pre = None
        self.next = None
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = {}
        self.tail = None
        self.head = None

    def get(self, key: int) -> int:
        cur = None
        if key in self.dic: cur = self.dic[key]        
        if cur:
            if len(self.dic) == 1:return cur.val
            if self.tail == cur: return cur.val
            if self.head == cur: self.head = cur.next
            if cur.next: cur.next.pre = cur.pre
            if cur.pre: cur.pre.next = cur.next

            cur.next = None
            cur.pre = self.tail
            self.tail.next = cur
            self.tail = cur
            return cur.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if self.cap <= 0:
            return
        cur = None
        if key in self.dic: cur = self.dic[key]
            
        if cur:
            self.get(key)
            cur.val = value
        else:
            node = Node(value,key)
            if len(self.dic) >= self.cap:
                deleteNode = self.head
                if self.head == self.tail:
                    self.head = node
                    self.tail = node
                else:
                    self.head = self.head.next
                    self.tail.next = node
                    node.pre = self.tail
                    self.head.pre = None
                    self.tail = self.tail.next
                self.dic.pop(deleteNode.key)
                deleteNode.pre = None
                deleteNode.next = None
                self.dic[key] = node
            else:
                if self.tail:
                    self.tail.next = node
                    node.pre = self.tail
                    self.tail = self.tail.next
                else:
                    self.head = node
                    self.tail = node
                self.dic[key] = node








            

            

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
obj.put(3,3)
print(obj.get(2))
obj.put(4,4)
obj.get(1)
print(obj.get(3))
print(obj.get(4))






# m = {}
# m[1] = 1
# print(m[1])

