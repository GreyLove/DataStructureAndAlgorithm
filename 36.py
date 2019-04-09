# #// 面试题36：二叉搜索树与双向链表
# #// 题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求
# #// 不能创建任何新的结点，只能调整树中结点指针的指向。

def ConvertNode(root,last:list):
    if not root:
        return
    
    ConvertNode(root.left,last)
    lastNode = last[0]
    root.left = lastNode
    if lastNode:
        lastNode.right = root
    last[0] = root
    ConvertNode(root.right,last)
    return last[0]




#// ====================测试代码====================

class BinaryTreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def CreateBinaryTreeNode(val):
    return BinaryTreeNode(val)

def ConnectTreeNodes(pParent, pLeft, pRight):
    if(pParent != None):
        pParent.left = pLeft
        pParent.right = pRight

def PrintDoubleLinkedList(pHeadOfList):

    pNode = pHeadOfList

    print("\nThe nodes from right to left are:\n")
    while(pNode != None):
    
        print("%d\t", pNode.val)

        if(pNode.left == None):
            break
        pNode = pNode.left

    
    print("The nodes from left to right are:\n")
    while(pNode != None):
    
        print("%d " % (pNode.val))

        if pNode.right == None:
            break
        pNode = pNode.right
    

    print("\n")


def DestroyList(pHeadOfList):

    pNode = pHeadOfList
    while(pNode != None):
    
        pNext = pNode.right

        pNode = pNext

def PrintTree(pRootOfTree):
    if not pRootOfTree:
        return
    PrintTree(pRootOfTree.left)
    print(pRootOfTree.val)
    PrintTree(pRootOfTree.right)


def Test(testName, pRootOfTree):

    if(testName != None):
        print("%s begins:\n", testName)

    PrintTree(pRootOfTree)

    pHeadOfList = ConvertNode(pRootOfTree,[None])

    PrintDoubleLinkedList(pHeadOfList)


#//            10
#//         /      \
#//        6        14
#//       /\        /\
#//      4  8     12  16
def Test1():

    pNode10 = CreateBinaryTreeNode(10)
    pNode6 = CreateBinaryTreeNode(6)
    pNode14 = CreateBinaryTreeNode(14)
    pNode4 = CreateBinaryTreeNode(4)
    pNode8 = CreateBinaryTreeNode(8)
    pNode12 = CreateBinaryTreeNode(12)
    pNode16 = CreateBinaryTreeNode(16)

    ConnectTreeNodes(pNode10, pNode6, pNode14)
    ConnectTreeNodes(pNode6, pNode4, pNode8)
    ConnectTreeNodes(pNode14, pNode12, pNode16)

    Test("Test1", pNode10)



#//               5
#//              /
#//             4
#//            /
#//           3
#//          /
#//         2
#//        /
#//       1
def Test2():

    pNode5 = CreateBinaryTreeNode(5)
    pNode4 = CreateBinaryTreeNode(4)
    pNode3 = CreateBinaryTreeNode(3)
    pNode2 = CreateBinaryTreeNode(2)
    pNode1 = CreateBinaryTreeNode(1)

    ConnectTreeNodes(pNode5, pNode4, None)
    ConnectTreeNodes(pNode4, pNode3, None)
    ConnectTreeNodes(pNode3, pNode2, None)
    ConnectTreeNodes(pNode2, pNode1, None)

    Test("Test2", pNode5)



#// 1
#//  \
#//   2
#//    \
#//     3
#//      \
#//       4
#//        \
#//         5
def Test3():

    pNode1 = CreateBinaryTreeNode(1)
    pNode2 = CreateBinaryTreeNode(2)
    pNode3 = CreateBinaryTreeNode(3)
    pNode4 = CreateBinaryTreeNode(4)
    pNode5 = CreateBinaryTreeNode(5)

    ConnectTreeNodes(pNode1, None, pNode2)
    ConnectTreeNodes(pNode2, None, pNode3)
    ConnectTreeNodes(pNode3, None, pNode4)
    ConnectTreeNodes(pNode4, None, pNode5)

    Test("Test3", pNode1)



#// 树中只有1个结点
def Test4():

    pNode1 = CreateBinaryTreeNode(1)
    Test("Test4", pNode1)


#// 树中没有结点
def Test5():

    Test("Test5", None)



Test1()
Test2()
Test3()
Test4()
Test5()
