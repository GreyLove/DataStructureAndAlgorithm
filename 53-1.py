# #// 面试题52：两个链表的第一个公共结点
# #// 题目：输入两个链表，找出它们的第一个公共结点。

from MyList import *


def FindFirstCommonNode(pHead1,pHead2):
    if not pHead1 or not pHead2:
        return
    
    cur = pHead1
    l1 = 0
    while cur:
        l1 += 1
        cur = cur.m_pNext
    
    cur = pHead2
    l2 = 0
    while cur:
        l2 += 1
        cur = cur.m_pNext
    
    diff = l1-l2

    if diff >= 0:
        cur1 = pHead1
        for _ in range(diff):
            cur1 = cur1.m_pNext
        cur2  = pHead2
    else:
        cur2 = pHead2
        for _ in range(diff):
            cur2 = cur2.m_pNext
        cur1 = pHead1
        
    while cur1 and cur2:
        if cur1 == cur2:
            return cur1
        cur1 = cur1.m_pNext
        cur2 = cur2.m_pNext
    
    return None
        
        



# #// ====================测试代码====================

def Test(testName, pHead1, pHead2, pExpected):

    if(testName != None):
        print("%s begins: "% testName)

    pResult = FindFirstCommonNode(pHead1, pHead2)
    if(pResult == pExpected):
        print("Passed.\n")
    else:
        print("Failed.\n")


#// 第一个公共结点在链表中间
#// 1 - 2 - 3 \
#//            6 - 7
#//     4 - 5 /
def Test1():

    pNode1 = CreateListNode(1)
    pNode2 = CreateListNode(2)
    pNode3 = CreateListNode(3)
    pNode4 = CreateListNode(4)
    pNode5 = CreateListNode(5)
    pNode6 = CreateListNode(6)
    pNode7 = CreateListNode(7)

    ConnectListNodes(pNode1, pNode2)
    ConnectListNodes(pNode2, pNode3)
    ConnectListNodes(pNode3, pNode6)
    ConnectListNodes(pNode4, pNode5)
    ConnectListNodes(pNode5, pNode6)
    ConnectListNodes(pNode6, pNode7)

    Test("Test1", pNode1, pNode4, pNode6)

    #DestroyNode(pNode1)
    #DestroyNode(pNode2)
    #DestroyNode(pNode3)
    #DestroyNode(pNode4)
    #DestroyNode(pNode5)
    #DestroyNode(pNode6)
    #DestroyNode(pNode7)


#// 没有公共结点
#// 1 - 2 - 3 - 4
#//            
#// 5 - 6 - 7
def Test2():

    pNode1 = CreateListNode(1)
    pNode2 = CreateListNode(2)
    pNode3 = CreateListNode(3)
    pNode4 = CreateListNode(4)
    pNode5 = CreateListNode(5)
    pNode6 = CreateListNode(6)
    pNode7 = CreateListNode(7)

    ConnectListNodes(pNode1, pNode2)
    ConnectListNodes(pNode2, pNode3)
    ConnectListNodes(pNode3, pNode4)
    ConnectListNodes(pNode5, pNode6)
    ConnectListNodes(pNode6, pNode7)

    Test("Test2", pNode1, pNode5, None)

    #DestroyList(pNode1)
    #DestroyList(pNode5)


#// 公共结点是最后一个结点
#// 1 - 2 - 3 - 4 \
#//                7
#//         5 - 6 /
def Test3():

    pNode1 = CreateListNode(1)
    pNode2 = CreateListNode(2)
    pNode3 = CreateListNode(3)
    pNode4 = CreateListNode(4)
    pNode5 = CreateListNode(5)
    pNode6 = CreateListNode(6)
    pNode7 = CreateListNode(7)

    ConnectListNodes(pNode1, pNode2)
    ConnectListNodes(pNode2, pNode3)
    ConnectListNodes(pNode3, pNode4)
    ConnectListNodes(pNode4, pNode7)
    ConnectListNodes(pNode5, pNode6)
    ConnectListNodes(pNode6, pNode7)

    Test("Test3", pNode1, pNode5, pNode7)

    #DestroyNode(pNode1)
    #DestroyNode(pNode2)
    #DestroyNode(pNode3)
    #DestroyNode(pNode4)
    #DestroyNode(pNode5)
    #DestroyNode(pNode6)
    #DestroyNode(pNode7)


#// 公共结点是第一个结点
#// 1 - 2 - 3 - 4 - 5
#// 两个链表完全重合   
def Test4():

    pNode1 = CreateListNode(1)
    pNode2 = CreateListNode(2)
    pNode3 = CreateListNode(3)
    pNode4 = CreateListNode(4)
    pNode5 = CreateListNode(5)

    ConnectListNodes(pNode1, pNode2)
    ConnectListNodes(pNode2, pNode3)
    ConnectListNodes(pNode3, pNode4)
    ConnectListNodes(pNode4, pNode5)

    Test("Test4", pNode1, pNode1, pNode1)

    #DestroyList(pNode1)


#// 输入的两个链表有一个空链表
def Test5():

    pNode1 = CreateListNode(1)
    pNode2 = CreateListNode(2)
    pNode3 = CreateListNode(3)
    pNode4 = CreateListNode(4)
    pNode5 = CreateListNode(5)

    ConnectListNodes(pNode1, pNode2)
    ConnectListNodes(pNode2, pNode3)
    ConnectListNodes(pNode3, pNode4)
    ConnectListNodes(pNode4, pNode5)

    Test("Test5", None, pNode1, None)

    #DestroyList(pNode1)


#// 输入的两个链表有一个空链表
def Test6():

    Test("Test6", None, None, None)





Test1()
Test2()
Test3()
Test4()
Test5()
Test6()
