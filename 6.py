# // 面试题6：从尾到头打印链表
# // 题目：输入一个链表的头结点，从尾到头反过来打印出每个结点的值。


class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None
        
def createList(list = []):
    if not list or not len(list):
        return
    head = Node(list[0])
    cur = head
    for i in range(1,len(list)):
        node = Node(list[i])
        cur.next = node
        cur = cur.next
    return head

# 一 用栈
# 二 递归

def printReverseList(head):
    if not head:
        return

    printReverseList(head.next)
    print(head.val)


def Test(list):
    head = createList(list)
    printReverseList(head)

Test([1,2,3,4,5])

Test([5,4,3,2,1])
