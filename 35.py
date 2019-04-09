# #// 面试题35：复杂链表的复制
# #// 题目：请实现函数ComplexListNode* Clone(ComplexListNode* pHead)，复
# #// 制一个复杂链表。在复杂链表中，每个结点除了有一个m_pNext指针指向下一个
# #// 结点外，还有一个m_pSibling 指向链表中的任意结点或者None。


def Clone(pHead):
    if not pHead:
        return

    cur = pHead
    
    while cur:
        node = ComplexListNode(cur.val)
        node.next = cur.next
        cur.next = node
        cur = cur.next.next
    
    # original = pHead
    # copy = pHead.next

    cur = pHead
    while cur:
        if cur.sibling:
            cur.next.sibling = cur.sibling.next
        
        cur = cur.next.next
    

    original = pHead
    copy = pHead.next
    newHead = copy
    while original:
        original.next = copy.next
        original = original.next
        if original:
            copy.next = original.next
            copy = copy.next

    return newHead 



#// ====================测试代码====================

class ComplexListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None
        self.sibling = None

def BuildNodes(pNode,pNext,pSibling):
        if(pNode != None):
            pNode.next = pNext
            pNode.sibling = pSibling

def PrintList(pHead):
    pNode = pHead
    while(pNode != None):

        # print("node: %d.\n"% pNode.val)
        v1 = ("node: %d.--"% pNode.val)
        if(pNode.sibling != None):
            # print("sibling: %d.\n"% pNode.sibling.val)
            v2 = ("sibling: %d.--"% pNode.sibling.val)
        else:
            # print("sibling: None.\n")
            v2 = ("sibling: None.--\n")
        print(v1+v2)
        pNode = pNode.next

def CreateNode(val):
    return ComplexListNode(val)


def Test(testName, pHead):

    if(testName != None):
        print("%s begins:\n"% testName)

    print("The original list is:\n")
    PrintList(pHead)

    pClonedHead = Clone(pHead)

    print("The cloned list is:\n")
    PrintList(pClonedHead)


#//          -----------------
#//         \|/              |
#//  1-------2-------3-------4-------5
#//  |       |      /|\             /|\
#//  --------+--------               |
#//          -------------------------
def Test1():

    pNode1 = CreateNode(1)
    pNode2 = CreateNode(2)
    pNode3 = CreateNode(3)
    pNode4 = CreateNode(4)
    pNode5 = CreateNode(5)

    BuildNodes(pNode1, pNode2, pNode3)
    BuildNodes(pNode2, pNode3, pNode5)
    BuildNodes(pNode3, pNode4, None)
    BuildNodes(pNode4, pNode5, pNode2)

    Test("Test1", pNode1)


#// m_pSibling指向结点自身
#//          -----------------
#//         \|/              |
#//  1-------2-------3-------4-------5
#//         |       | /|\           /|\
#//         |       | --             |
#//         |------------------------|
def Test2():

    pNode1 = CreateNode(1)
    pNode2 = CreateNode(2)
    pNode3 = CreateNode(3)
    pNode4 = CreateNode(4)
    pNode5 = CreateNode(5)

    BuildNodes(pNode1, pNode2, None)
    BuildNodes(pNode2, pNode3, pNode5)
    BuildNodes(pNode3, pNode4, pNode3)
    BuildNodes(pNode4, pNode5, pNode2)

    Test("Test2", pNode1)


#// m_pSibling形成环
#//          -----------------
#//         \|/              |
#//  1-------2-------3-------4-------5
#//          |              /|\
#//          |               |
#//          |---------------|
def Test3():

    pNode1 = CreateNode(1)
    pNode2 = CreateNode(2)
    pNode3 = CreateNode(3)
    pNode4 = CreateNode(4)
    pNode5 = CreateNode(5)

    BuildNodes(pNode1, pNode2, None)
    BuildNodes(pNode2, pNode3, pNode4)
    BuildNodes(pNode3, pNode4, None)
    BuildNodes(pNode4, pNode5, pNode2)

    Test("Test3", pNode1)


#// 只有一个结点
def Test4():

    pNode1 = CreateNode(1)
    BuildNodes(pNode1, None, pNode1)

    Test("Test4", pNode1)


#// 鲁棒性测试
def Test5():

    Test("Test5", None)



Test1()
Test2()
Test3()
Test4()
Test5()
