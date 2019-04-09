# / 面试题25：合并两个排序的链表
# #// 题目：输入两个递增排序的链表，合并这两个链表并使新链表中的结点仍然是按
# #// 照递增排序的。例如输入图3.11中的链表1和链表2，则合并之后的升序链表如链
# #// 表3所示。

from MyList import *


def Merge(pHead1,pHead2):
    if not pHead1 and not pHead2:return
    elif not pHead1:
        return pHead2
    elif not pHead2:
        return pHead1


    i = pHead1
    j = pHead2
    newHead = None
    cur = newHead
    while i != None and j != None:
        if i.m_nValue < j.m_nValue:
            if cur == None:
                newHead = i
                cur = newHead
            else:
                cur.m_pNext = i
                cur = cur.m_pNext
            i = i.m_pNext
        else:
            if cur == None:
                newHead = j
                cur = newHead
            else:
                cur.m_pNext = j
                cur = cur.m_pNext
            j = j.m_pNext
    
    while i:
        cur.m_pNext = i
        i = i.m_pNext
        cur = cur.m_pNext

    while j:
        cur.m_pNext = j
        j = j.m_pNext
        cur = cur.m_pNext   
    
    return newHead


#// ====================测试代码====================
def Test(testName, pHead1, pHead2):

    if(testName != None):
        print("%s begins:\n"% testName)

    print("The first list is:\n")
    PrintList(pHead1)

    print("The second list is:\n")
    PrintList(pHead2)

    print("The merged list is:\n")
    pMergedHead = Merge(pHead1, pHead2)
    PrintList(pMergedHead)
    
    print("\n\n")

    return pMergedHead


#// list1: 1->3->5
#// list2: 2->4->6
def Test1():

    pNode1 = CreateListNode(1)
    pNode3 = CreateListNode(3)
    pNode5 = CreateListNode(5)

    ConnectListNodes(pNode1, pNode3)
    ConnectListNodes(pNode3, pNode5)

    pNode2 = CreateListNode(2)
    pNode4 = CreateListNode(4)
    pNode6 = CreateListNode(6)

    ConnectListNodes(pNode2, pNode4)
    ConnectListNodes(pNode4, pNode6)

    pMergedHead = Test("Test1", pNode1, pNode2)

    DestroyList(pMergedHead)


#// 两个链表中有重复的数字
#// list1: 1->3->5
#// list2: 1->3->5
def Test2():

    pNode1 = CreateListNode(1)
    pNode3 = CreateListNode(3)
    pNode5 = CreateListNode(5)

    ConnectListNodes(pNode1, pNode3)
    ConnectListNodes(pNode3, pNode5)

    pNode2 = CreateListNode(1)
    pNode4 = CreateListNode(3)
    pNode6 = CreateListNode(5)

    ConnectListNodes(pNode2, pNode4)
    ConnectListNodes(pNode4, pNode6)

    pMergedHead = Test("Test2", pNode1, pNode2)

    DestroyList(pMergedHead)


#// 两个链表都只有一个数字
#// list1: 1
#// list2: 2
def Test3():

    pNode1 = CreateListNode(1)
    pNode2 = CreateListNode(2)

    pMergedHead = Test("Test3", pNode1, pNode2)

    DestroyList(pMergedHead)


#// 一个链表为空链表
#// list1: 1->3->5
#// list2: 空链表
def Test4():

    pNode1 = CreateListNode(1)
    pNode3 = CreateListNode(3)
    pNode5 = CreateListNode(5)

    ConnectListNodes(pNode1, pNode3)
    ConnectListNodes(pNode3, pNode5)

    pMergedHead = Test("Test4", pNode1, None)

    DestroyList(pMergedHead)


#// 两个链表都为空链表
#// list1: 空链表
#// list2: 空链表
def Test5():

    pMergedHead = Test("Test5", None, None)



Test1()
Test2()
Test3()
Test4()
Test5()


