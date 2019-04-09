# #// 面试题8：二叉树的下一个结点
# #// 题目：给定一棵二叉树和其中的一个结点，如何找出中序遍历顺序的下一个结点？
# #// 树中的结点除了有两个分别指向左右子结点的指针以外，还有一个指向父结点的指针。




def GetNext(node):
    if not node:
        return
    
    if node.right:
        cur = node.right
        while cur.left:
            cur = cur.left
        
        return cur
    else:
        if node.parent and node.parent.left == node:
            return node.parent
        elif node.parent and node.parent.right == node:
            cur = node
            while cur.parent and cur.parent.right == cur:
                cur = cur.parent
            
            if cur.parent == None:
                return None
            
            return cur.parent
    





#// ==================== 辅助代码用来构建二叉树 ====================

class TreeNode(object):
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None
        self.parent = None

def CreateBinaryTreeNode(value):
    return TreeNode(value)


def ConnectTreeNodes(pParent, pLeft, pRight):

    if(pParent != None):
    
        pParent.left = pLeft
        pParent.right = pRight

        if(pLeft != None):
            pLeft.parent = pParent
        if(pRight != None):
            pRight.parent = pParent
    


def PrintTreeNode(pNode):

    if(pNode != None):
    
        print("value of this node is: %d\n" % pNode.val)

        if(pNode.left != None):
            print("value of its left child is: %d.\n", pNode.left.val)
        else:
            print("left child is null.\n")

        if(pNode.right != None):
            print("value of its right child is: %d.\n", pNode.right.val)
        else:
            print("right child is null.\n")
    
    else:
    
        print("this node is null.\n")
    

    print("\n")


def PrintTree(pRoot):

    PrintTreeNode(pRoot)

    if(pRoot != None):
    
        if(pRoot.left != None):
            PrintTree(pRoot.left)

        if(pRoot.right != None):
            PrintTree(pRoot.right)
    


#// ====================测试代码====================
def Test(testName, pNode, expected):

    if(testName != None):
        print("%s begins: "% testName)

    pNext = GetNext(pNode)
    if(pNext == expected):
        print("Passed.\n")
    else:
        print("FAILED.\n")


#//            8
#//        6      10
#//       5 7    9  11
def Test1_7():

    pNode8 = CreateBinaryTreeNode(8)
    pNode6 = CreateBinaryTreeNode(6)
    pNode10 = CreateBinaryTreeNode(10)
    pNode5 = CreateBinaryTreeNode(5)
    pNode7 = CreateBinaryTreeNode(7)
    pNode9 = CreateBinaryTreeNode(9)
    pNode11 = CreateBinaryTreeNode(11)

    ConnectTreeNodes(pNode8, pNode6, pNode10)
    ConnectTreeNodes(pNode6, pNode5, pNode7)
    ConnectTreeNodes(pNode10, pNode9, pNode11)

    Test("Test1", pNode8, pNode9)
    Test("Test2", pNode6, pNode7)
    Test("Test3", pNode10, pNode11)
    Test("Test4", pNode5, pNode6)
    Test("Test5", pNode7, pNode8)
    Test("Test6", pNode9, pNode10)
    Test("Test7", pNode11, None)

    #DestroyTree(pNode8)


#//            5
#//          4
#//        3
#//      2
def Test8_11():

    pNode5 = CreateBinaryTreeNode(5)
    pNode4 = CreateBinaryTreeNode(4)
    pNode3 = CreateBinaryTreeNode(3)
    pNode2 = CreateBinaryTreeNode(2)

    ConnectTreeNodes(pNode5, pNode4, None)
    ConnectTreeNodes(pNode4, pNode3, None)
    ConnectTreeNodes(pNode3, pNode2, None)

    Test("Test8", pNode5, None)
    Test("Test9", pNode4, pNode5)
    Test("Test10", pNode3, pNode4)
    Test("Test11", pNode2, pNode3)

    #DestroyTree(pNode5)


#//        2
#//         3
#//          4
#//           5
def Test12_15():

    pNode2 = CreateBinaryTreeNode(2)
    pNode3 = CreateBinaryTreeNode(3)
    pNode4 = CreateBinaryTreeNode(4)
    pNode5 = CreateBinaryTreeNode(5)

    ConnectTreeNodes(pNode2, None, pNode3)
    ConnectTreeNodes(pNode3, None, pNode4)
    ConnectTreeNodes(pNode4, None, pNode5)

    Test("Test12", pNode5, None)
    Test("Test13", pNode4, pNode5)
    Test("Test14", pNode3, pNode4)
    Test("Test15", pNode2, pNode3)

    #DestroyTree(pNode2)


def Test16():

    pNode5 = CreateBinaryTreeNode(5)

    Test("Test16", pNode5, None)

    #DestroyTree(pNode5)



Test1_7()
Test8_11()
Test12_15()
Test16()

