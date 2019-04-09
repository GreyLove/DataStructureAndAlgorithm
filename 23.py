# #// 面试题23：链表中环的入口结点
# #// 题目：一个链表中包含环，如何找出环的入口结点？例如，在图3.8的链表中，
# #// 环的入口结点是结点3。

def EntryNodeOfLoop(pHead):
    if not pHead:
        return

    slow = pHead
    fast = pHead.m_pNext

    while slow != fast and fast != None and fast.m_pNext != None:
        slow = slow.m_pNext
        fast = fast.m_pNext.m_pNext
    
    if fast == None or fast.m_pNext == None:
        return None #无环
    
    fast = slow.m_pNext
    k = 1
    while slow != fast:
        fast = fast.m_pNext
        k += 1
    
    slow = pHead
    fast = pHead
    for _ in range(k):
        fast = fast.m_pNext
    
    while slow != fast:
        slow = slow.m_pNext
        fast = fast.m_pNext
    
    return slow
        




# #// ==================== Test Code ====================

class ListNode(object):
    def __init__(self, val):
        self.m_nValue = val
        self.m_pNext = None

def CreateListNode(value):
    return ListNode(value)

def PrintListNode(pNode):

    if(pNode == None):
    
        print("The node is None\n")
    
    else:
    
        print("The key in node is %d.\n"% pNode.m_nValue)
    



def ConnectListNodes(pCurrent, pNext):

    if(pCurrent == None):
    
        print("Error to connect two nodes.\n")
        
    pCurrent.m_pNext = pNext

def Test(testName, pHead, entryNode):

    if(testName != None):
        print("%s begins: "% testName)

    if(EntryNodeOfLoop(pHead) == entryNode):
        print("Passed.\n")
    else:
        print("FAILED.\n")


#// A list has a node, without a loop
def Test1():

    pNode1 = CreateListNode(1)

    Test("Test1", pNode1, None)

    #DestroyList(pNode1)


#// A list has a node, with a loop
def Test2():

    pNode1 = CreateListNode(1)
    ConnectListNodes(pNode1, pNode1)

    Test("Test2", pNode1, pNode1)

    #delete pNode1
    pNode1 = None


#// A list has multiple nodes, with a loop 
def Test3():

    pNode1 = CreateListNode(1)
    pNode2 = CreateListNode(2)
    pNode3 = CreateListNode(3)
    pNode4 = CreateListNode(4)
    pNode5 = CreateListNode(5)

    ConnectListNodes(pNode1, pNode2)
    ConnectListNodes(pNode2, pNode3)
    ConnectListNodes(pNode3, pNode4)
    ConnectListNodes(pNode4, pNode5)
    ConnectListNodes(pNode5, pNode3)

    Test("Test3", pNode1, pNode3)

    #delete pNode1
    pNode1 = None
    #delete pNode2
    pNode2 = None
    #delete pNode3
    pNode3 = None
    #delete pNode4
    pNode4 = None
    #delete pNode5
    pNode5 = None


#// A list has multiple nodes, with a loop 
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
    ConnectListNodes(pNode5, pNode1)

    Test("Test4", pNode1, pNode1)

    #delete pNode1
    pNode1 = None
    #delete pNode2
    pNode2 = None
    #delete pNode3
    pNode3 = None
    #delete pNode4
    pNode4 = None
    #delete pNode5
    pNode5 = None


#// A list has multiple nodes, with a loop 
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
    ConnectListNodes(pNode5, pNode5)

    Test("Test5", pNode1, pNode5)

    #delete pNode1
    pNode1 = None
    #delete pNode2
    pNode2 = None
    #delete pNode3
    pNode3 = None
    #delete pNode4
    pNode4 = None
    #delete pNode5
    pNode5 = None


#// A list has multiple nodes, without a loop 
def Test6():

    pNode1 = CreateListNode(1)
    pNode2 = CreateListNode(2)
    pNode3 = CreateListNode(3)
    pNode4 = CreateListNode(4)
    pNode5 = CreateListNode(5)

    ConnectListNodes(pNode1, pNode2)
    ConnectListNodes(pNode2, pNode3)
    ConnectListNodes(pNode3, pNode4)
    ConnectListNodes(pNode4, pNode5)

    Test("Test6", pNode1, None)

    #DestroyList(pNode1)


#// Empty list
def Test7():

    Test("Test7", None, None)



Test1()
Test2()
Test3()
Test4()
Test5()
Test6()
Test7()


