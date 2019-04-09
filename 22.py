# #// 面试题22：链表中倒数第k个结点
# #// 题目：输入一个链表，输出该链表中倒数第k个结点。为了符合大多数人的习惯，
# #// 本题从1开始计数，即链表的尾结点是倒数第1个结点。例如一个链表有6个结点，
# #// 从头结点开始它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个结点是
# #// 值为4的结点。
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



def FindKthToTail(node,k):
    if not node or k < 1:
        return
    
    i = 0
    p = node
    while p!=None and i < k:
        p = p.m_pNext
        i+=1
    if i < k:
        return None
    q = node
    while  p != None:
        q = q.m_pNext
        p = p.m_pNext
    
    return q



#// ====================测试代码====================
#// 测试要找的结点在链表中间
def Test1():

    print("=====Test1 starts:=====\n")
    pNode1 = CreateListNode(1)
    pNode2 = CreateListNode(2)
    pNode3 = CreateListNode(3)
    pNode4 = CreateListNode(4)
    pNode5 = CreateListNode(5)

    ConnectListNodes(pNode1, pNode2)
    ConnectListNodes(pNode2, pNode3)
    ConnectListNodes(pNode3, pNode4)
    ConnectListNodes(pNode4, pNode5)

    print("expected result: 4.\n")
    pNode = FindKthToTail(pNode1, 2)
    PrintListNode(pNode)

    #DestroyList(pNode1)


#// 测试要找的结点是链表的尾结点
def Test2():

    print("=====Test2 starts:=====\n")
    pNode1 = CreateListNode(1)
    pNode2 = CreateListNode(2)
    pNode3 = CreateListNode(3)
    pNode4 = CreateListNode(4)
    pNode5 = CreateListNode(5)

    ConnectListNodes(pNode1, pNode2)
    ConnectListNodes(pNode2, pNode3)
    ConnectListNodes(pNode3, pNode4)
    ConnectListNodes(pNode4, pNode5)

    print("expected result: 5.\n")
    pNode = FindKthToTail(pNode1, 1)
    PrintListNode(pNode)

    #DestroyList(pNode1)


#// 测试要找的结点是链表的头结点
def Test3():

    print("=====Test3 starts:=====\n")
    pNode1 = CreateListNode(1)
    pNode2 = CreateListNode(2)
    pNode3 = CreateListNode(3)
    pNode4 = CreateListNode(4)
    pNode5 = CreateListNode(5)

    ConnectListNodes(pNode1, pNode2)
    ConnectListNodes(pNode2, pNode3)
    ConnectListNodes(pNode3, pNode4)
    ConnectListNodes(pNode4, pNode5)

    print("expected result: 1.\n")
    pNode = FindKthToTail(pNode1, 5)
    PrintListNode(pNode)

    #DestroyList(pNode1)


#// 测试空链表
def Test4():

    print("=====Test4 starts:=====\n")
    print("expected result: None.\n")
    pNode = FindKthToTail(None, 100)
    PrintListNode(pNode)


#// 测试输入的第二个参数大于链表的结点总数
def Test5():

    print("=====Test5 starts:=====\n")
    pNode1 = CreateListNode(1)
    pNode2 = CreateListNode(2)
    pNode3 = CreateListNode(3)
    pNode4 = CreateListNode(4)
    pNode5 = CreateListNode(5)

    ConnectListNodes(pNode1, pNode2)
    ConnectListNodes(pNode2, pNode3)
    ConnectListNodes(pNode3, pNode4)
    ConnectListNodes(pNode4, pNode5)

    print("expected result: None.\n")
    pNode = FindKthToTail(pNode1, 6)
    PrintListNode(pNode)

    #DestroyList(pNode1)


#// 测试输入的第二个参数为0
def Test6():

    print("=====Test6 starts:=====\n")
    pNode1 = CreateListNode(1)
    pNode2 = CreateListNode(2)
    pNode3 = CreateListNode(3)
    pNode4 = CreateListNode(4)
    pNode5 = CreateListNode(5)

    ConnectListNodes(pNode1, pNode2)
    ConnectListNodes(pNode2, pNode3)
    ConnectListNodes(pNode3, pNode4)
    ConnectListNodes(pNode4, pNode5)

    print("expected result: None.\n")
    pNode = FindKthToTail(pNode1, 0)
    PrintListNode(pNode)

    #DestroyList(pNode1)



Test1()
Test2()
Test3()
Test4()
Test5()
Test6()


