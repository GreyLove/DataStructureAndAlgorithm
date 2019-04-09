# // 面试题27：二叉树的镜像
# // 题目：请完成一个函数，输入一个二叉树，该函数输出它的镜像。

from MyTree import *

def MirrorRecursively(root):
    if root == None:
        return
    
    tmp = root.left
    root.left = root.right
    root.right = tmp

    MirrorRecursively(root.left)
    MirrorRecursively(root.right)





#// ====================测试代码====================
#// 测试完全二叉树：除了叶子节点，其他节点都有两个子节点
#//            8
#//        6      10
#//       5 7    9  11
def Test1():

    print("=====Test1 starts:=====\n")
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

    #PrintTree(pNode8)

    print("=====Test1: MirrorRecursively=====\n")
    MirrorRecursively(pNode8)
    #PrintTree(pNode8)

    print("=====Test1: #MirrorIteratively=====\n")
    #MirrorIteratively(pNode8)
    #PrintTree(pNode8)

    #DestroyTree(pNode8)


#// 测试二叉树：出叶子结点之外，左右的结点都有且只有一个左子结点
#//            8
#//          7   
#//        6 
#//      5
#//    4
def Test2():

    print("=====Test2 starts:=====\n")
    pNode8 = CreateBinaryTreeNode(8)
    pNode7 = CreateBinaryTreeNode(7)
    pNode6 = CreateBinaryTreeNode(6)
    pNode5 = CreateBinaryTreeNode(5)
    pNode4 = CreateBinaryTreeNode(4)

    ConnectTreeNodes(pNode8, pNode7, None)
    ConnectTreeNodes(pNode7, pNode6, None)
    ConnectTreeNodes(pNode6, pNode5, None)
    ConnectTreeNodes(pNode5, pNode4, None)

    #PrintTree(pNode8)

    print("=====Test2: MirrorRecursively=====\n")
    MirrorRecursively(pNode8)
    #PrintTree(pNode8)

    print("=====Test2: #MirrorIteratively=====\n")
    #MirrorIteratively(pNode8)
    #PrintTree(pNode8)

    #DestroyTree(pNode8)


#// 测试二叉树：出叶子结点之外，左右的结点都有且只有一个右子结点
#//            8
#//             7   
#//              6 
#//               5
#//                4
def Test3():

    print("=====Test3 starts:=====\n")
    pNode8 = CreateBinaryTreeNode(8)
    pNode7 = CreateBinaryTreeNode(7)
    pNode6 = CreateBinaryTreeNode(6)
    pNode5 = CreateBinaryTreeNode(5)
    pNode4 = CreateBinaryTreeNode(4)

    ConnectTreeNodes(pNode8, None, pNode7)
    ConnectTreeNodes(pNode7, None, pNode6)
    ConnectTreeNodes(pNode6, None, pNode5)
    ConnectTreeNodes(pNode5, None, pNode4)

    #PrintTree(pNode8)

    print("=====Test3: MirrorRecursively=====\n")
    MirrorRecursively(pNode8)
    #PrintTree(pNode8)

    print("=====Test3: #MirrorIteratively=====\n")
    #MirrorIteratively(pNode8)
    #PrintTree(pNode8)

    #DestroyTree(pNode8)


#// 测试空二叉树：根结点为空指针
def Test4():

    print("=====Test4 starts:=====\n")
    pNode = None

    #PrintTree(pNode)

    print("=====Test4: MirrorRecursively=====\n")
    MirrorRecursively(pNode)
    #PrintTree(pNode)

    print("=====Test4: #MirrorIteratively=====\n")
    #MirrorIteratively(pNode)
    #PrintTree(pNode)


#// 测试只有一个结点的二叉树
def Test5():

    print("=====Test5 starts:=====\n")
    pNode8 = CreateBinaryTreeNode(8)

    #PrintTree(pNode8)

    print("=====Test4: MirrorRecursively=====\n")
    MirrorRecursively(pNode8)
    #PrintTree(pNode8)

    print("=====Test4: #MirrorIteratively=====\n")
    #MirrorIteratively(pNode8)
    #PrintTree(pNode8)


Test1()
Test2()
Test3()
Test4()
Test5()
