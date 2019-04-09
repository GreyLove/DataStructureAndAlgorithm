# // 面试题18（一）：在O(1)时间删除链表结点
# // 题目：给定单向链表的头指针和一个结点指针，定义一个函数在O(1)时间删除该
# // 结点。

class node(object):
    def __init__(self,val):
        self.val = val
        self.next = None


def deleteNode(root,node):
    if not root or not node:
        return
    
    if root == node and node.next == None:
        return
    elif node.next == None:
        cur = root
        while cur.next != node:
            cur = cur.next
        cur.next = None
    else:
        cur = node.next
        node.val = cur.val
        node.next = cur.next
        cur.next = None
    
    return root



cur = node(0)
root = cur
tmp = cur
for i in range(1,3):
    cur.next = node(i)
    cur = cur.next
    if i == 1:
        tmp = cur

root = deleteNode(root,tmp)
print(root)

# root = deleteNode(root,tmp)
# print(root)
