# #// 面试题18（二）：删除链表中重复的结点
# #// 题目：在一个排序的链表中，如何删除重复的结点？例如，在图3.4（a）中重复
# #// 结点被删除之后，链表如图3.4（b）所示。
class ListNode(object):
    def __init__(self, val):
        self.m_nValue = val
        self.m_pNext = None

def CreateListNode(value):
    return ListNode(value)

def ConnectListNodes(pCurrent, pNext):

    if(pCurrent == None):
    
        print("Error to connect two nodes.\n")
        
    pCurrent.m_pNext = pNext


def DeleteDuplication(pHead):
    if not pHead:
        return
    
    if pHead.m_pNext == None:
        return pHead
    
    i = pHead
    j = pHead.m_pNext

    while j:
        if i.m_nValue == j.m_nValue:
            while j and i.m_nValue == j.m_nValue:
                j = j.m_pNext
            if j:
                i.m_nValue = j.m_nValue
                i.m_pNext = j.m_pNext
                tmp = j
                j = j.m_pNext
                tmp.m_pNext = None
            else:
                if pHead == i:
                    pHead = None
                else:
                    cur = pHead
                    while cur.m_pNext != i:
                        cur = cur.m_pNext
                    cur.m_pNext = None
        else:
            i = i.m_pNext
            j = j.m_pNext
    
    return pHead




#// ====================测试代码====================
def Test(testName, pHead, expectedValues, expectedLength):

    if(testName != None):
        print("%s begins: "% testName)

    re = DeleteDuplication(pHead[0])

    index = 0
    pNode = re
    while(pNode != None and index < expectedLength):
    
        if(pNode.m_nValue != expectedValues[index]):
            break

        pNode = pNode.m_pNext
        index += 1
    

    if(pNode == None and index == expectedLength):
        print("Passed.\n")
    else:
        print("FAILED.\n")


#// 某些结点是重复的
def Test1():

    pNode1 = CreateListNode(1)
    pNode2 = CreateListNode(2)
    pNode3 = CreateListNode(3)
    pNode4 = CreateListNode(3)
    pNode5 = CreateListNode(4)
    pNode6 = CreateListNode(4)
    pNode7 = CreateListNode(5)

    ConnectListNodes(pNode1, pNode2)
    ConnectListNodes(pNode2, pNode3)
    ConnectListNodes(pNode3, pNode4)
    ConnectListNodes(pNode4, pNode5)
    ConnectListNodes(pNode5, pNode6)
    ConnectListNodes(pNode6, pNode7)

    pHead = pNode1

    expectedValues = [ 1, 2, 5 ]
    Test("Test1", [pHead], expectedValues, len(expectedValues))

    


#// 没有重复的结点
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
    ConnectListNodes(pNode4, pNode5)
    ConnectListNodes(pNode5, pNode6)
    ConnectListNodes(pNode6, pNode7)

    pHead = pNode1

    expectedValues = [ 1, 2, 3, 4, 5, 6, 7 ]
    Test("Test2", [pHead], expectedValues, len(expectedValues))

    


#// 除了一个结点之外其他所有结点的值都相同
def Test3():

    pNode1 = CreateListNode(1)
    pNode2 = CreateListNode(1)
    pNode3 = CreateListNode(1)
    pNode4 = CreateListNode(1)
    pNode5 = CreateListNode(1)
    pNode6 = CreateListNode(1)
    pNode7 = CreateListNode(2)

    ConnectListNodes(pNode1, pNode2)
    ConnectListNodes(pNode2, pNode3)
    ConnectListNodes(pNode3, pNode4)
    ConnectListNodes(pNode4, pNode5)
    ConnectListNodes(pNode5, pNode6)
    ConnectListNodes(pNode6, pNode7)

    pHead = pNode1

    expectedValues = [ 2 ]
    Test("Test3", [pHead], expectedValues, len(expectedValues))

    


#// 所有结点的值都相同
def Test4():

    pNode1 = CreateListNode(1)
    pNode2 = CreateListNode(1)
    pNode3 = CreateListNode(1)
    pNode4 = CreateListNode(1)
    pNode5 = CreateListNode(1)
    pNode6 = CreateListNode(1)
    pNode7 = CreateListNode(1)

    ConnectListNodes(pNode1, pNode2)
    ConnectListNodes(pNode2, pNode3)
    ConnectListNodes(pNode3, pNode4)
    ConnectListNodes(pNode4, pNode5)
    ConnectListNodes(pNode5, pNode6)
    ConnectListNodes(pNode6, pNode7)

    pHead = pNode1

    Test("Test4", [pHead], None, 0)

    


#// 所有结点都成对出现
def Test5():

    pNode1 = CreateListNode(1)
    pNode2 = CreateListNode(1)
    pNode3 = CreateListNode(2)
    pNode4 = CreateListNode(2)
    pNode5 = CreateListNode(3)
    pNode6 = CreateListNode(3)
    pNode7 = CreateListNode(4)
    pNode8 = CreateListNode(4)

    ConnectListNodes(pNode1, pNode2)
    ConnectListNodes(pNode2, pNode3)
    ConnectListNodes(pNode3, pNode4)
    ConnectListNodes(pNode4, pNode5)
    ConnectListNodes(pNode5, pNode6)
    ConnectListNodes(pNode6, pNode7)
    ConnectListNodes(pNode7, pNode8)

    pHead = pNode1

    Test("Test5", [pHead], None, 0)

    


#// 除了两个结点之外其他结点都成对出现
def Test6():

    pNode1 = CreateListNode(1)
    pNode2 = CreateListNode(1)
    pNode3 = CreateListNode(2)
    pNode4 = CreateListNode(3)
    pNode5 = CreateListNode(3)
    pNode6 = CreateListNode(4)
    pNode7 = CreateListNode(5)
    pNode8 = CreateListNode(5)

    ConnectListNodes(pNode1, pNode2)
    ConnectListNodes(pNode2, pNode3)
    ConnectListNodes(pNode3, pNode4)
    ConnectListNodes(pNode4, pNode5)
    ConnectListNodes(pNode5, pNode6)
    ConnectListNodes(pNode6, pNode7)
    ConnectListNodes(pNode7, pNode8)

    pHead = pNode1

    expectedValues = [ 2, 4 ]
    Test("Test6", [pHead], expectedValues, len(expectedValues))

    


#// 链表中只有两个不重复的结点
def Test7():

    pNode1 = CreateListNode(1)
    pNode2 = CreateListNode(2)

    ConnectListNodes(pNode1, pNode2)

    pHead = pNode1

    expectedValues = [ 1, 2 ]
    Test("Test7", [pHead], expectedValues, len(expectedValues))

    


#// 结点中只有一个结点
def Test8():

    pNode1 = CreateListNode(1)

    ConnectListNodes(pNode1, None)

    pHead = pNode1

    expectedValues = [ 1 ]
    Test("Test8", [pHead], expectedValues, len(expectedValues))

    


#// 结点中只有两个重复的结点
def Test9():

    pNode1 = CreateListNode(1)
    pNode2 = CreateListNode(1)

    ConnectListNodes(pNode1, pNode2)

    pHead = pNode1

    Test("Test9", [pHead], None, 0)

    


#// 空链表
def Test10():

    pHead = None

    Test("Test10", [pHead], None, 0)



Test1()
Test2()
Test3()
Test4()
Test5()
Test6()
Test7()
Test8()
Test9()
Test10()



