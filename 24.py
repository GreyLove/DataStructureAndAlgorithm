# #// 面试题24：反转链表
# #// 题目：定义一个函数，输入一个链表的头结点，反转该链表并输出反转后链表的
# #// 头结点。
from MyList import *

def ReverseList(pHead):
    if pHead == None or pHead.m_pNext == None:
        return pHead
    i = None
    j = pHead
    t = pHead.m_pNext

    while j:
        j.m_pNext = i
        i = j
        j = t
        if t:
            t = t.m_pNext
    
    return i

#// ====================测试代码====================
def Test(pHead):

    print("The original list is: \n")
    PrintList(pHead)

    pReversedHead = ReverseList(pHead)

    print("The reversed list is: \n")
    PrintList(pReversedHead)

    return pReversedHead


#// 输入的链表有多个结点
def Test1():

    pNode1 = CreateListNode(1)
    pNode2 = CreateListNode(2)
    pNode3 = CreateListNode(3)
    pNode4 = CreateListNode(4)
    pNode5 = CreateListNode(5)

    ConnectListNodes(pNode1, pNode2)
    ConnectListNodes(pNode2, pNode3)
    ConnectListNodes(pNode3, pNode4)
    ConnectListNodes(pNode4, pNode5)

    pReversedHead = Test(pNode1)

    DestroyList(pReversedHead)


#// 输入的链表只有一个结点
def Test2():

    pNode1 = CreateListNode(1)

    pReversedHead = Test(pNode1)

    DestroyList(pReversedHead)


#// 输入空链表
def Test3():

    Test(None)


Test1()
Test2()
Test3()


