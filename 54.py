# #// 面试题54：二叉搜索树的第k个结点
# #// 题目：给定一棵二叉搜索树，请找出其中的第k大的结点。

from MyTree import *

def KthNode(pRoot,k):
    if not pRoot:
        return

    root = KthNodeCore(pRoot,k,[1])
    return root
    

def KthNodeCore(pRoot,k,count:list):
    if not pRoot:
        return
    find = KthNodeCore(pRoot.left,k,count)
    if not find:
        if k == count[0]:
            return pRoot
        count[0] += 1
        find = KthNodeCore(pRoot.right,k,count)
    return find




#// ====================测试代码====================
def Test(testName, pRoot, k, isNull, expected):

    if(testName != None):
        print("%s begins: "% testName)

    pTarget = KthNode(pRoot, k)
    if((isNull and pTarget == None) or (pTarget and not isNull and pTarget.val == expected)):
        print("Passed.\n")
    else:
        print("FAILED.\n")


#//            8
#//        6      10
#//       5 7    9  11
def TestA():

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

    Test("TestA0", pNode8, 0, True, -1)
    Test("TestA1", pNode8, 1, False, 5)
    Test("TestA2", pNode8, 2, False, 6)
    Test("TestA3", pNode8, 3, False, 7)
    Test("TestA4", pNode8, 4, False, 8)
    Test("TestA5", pNode8, 5, False, 9)
    Test("TestA6", pNode8, 6, False, 10)
    Test("TestA7", pNode8, 7, False, 11)
    Test("TestA8", pNode8, 8, True, -1)

    #DestroyTree(pNode8)

    print("\n\n")


#//               5
#//              /
#//             4
#//            /
#//           3
#//          /
#//         2
#//        /
#//       1
def TestB():

    pNode5 = CreateBinaryTreeNode(5)
    pNode4 = CreateBinaryTreeNode(4)
    pNode3 = CreateBinaryTreeNode(3)
    pNode2 = CreateBinaryTreeNode(2)
    pNode1 = CreateBinaryTreeNode(1)

    ConnectTreeNodes(pNode5, pNode4, None)
    ConnectTreeNodes(pNode4, pNode3, None)
    ConnectTreeNodes(pNode3, pNode2, None)
    ConnectTreeNodes(pNode2, pNode1, None)

    Test("TestB0", pNode5, 0, True, -1)
    Test("TestB1", pNode5, 1, False, 1)
    Test("TestB2", pNode5, 2, False, 2)
    Test("TestB3", pNode5, 3, False, 3)
    Test("TestB4", pNode5, 4, False, 4)
    Test("TestB5", pNode5, 5, False, 5)
    Test("TestB6", pNode5, 6, True, -1)

    #DestroyTree(pNode5)

    print("\n\n")


#// 1
#//  \
#//   2
#//    \
#//     3
#//      \
#//       4
#//        \
#//         5
def TestC():

    pNode1 = CreateBinaryTreeNode(1)
    pNode2 = CreateBinaryTreeNode(2)
    pNode3 = CreateBinaryTreeNode(3)
    pNode4 = CreateBinaryTreeNode(4)
    pNode5 = CreateBinaryTreeNode(5)

    ConnectTreeNodes(pNode1, None, pNode2)
    ConnectTreeNodes(pNode2, None, pNode3)
    ConnectTreeNodes(pNode3, None, pNode4)
    ConnectTreeNodes(pNode4, None, pNode5)

    Test("TestC0", pNode1, 0, True, -1)
    Test("TestC1", pNode1, 1, False, 1)
    Test("TestC2", pNode1, 2, False, 2)
    Test("TestC3", pNode1, 3, False, 3)
    Test("TestC4", pNode1, 4, False, 4)
    Test("TestC5", pNode1, 5, False, 5)
    Test("TestC6", pNode1, 6, True, -1)

    #DestroyTree(pNode1)

    print("\n\n")


#// There is only one node in a tree
def TestD():

    pNode1 = CreateBinaryTreeNode(1)

    Test("TestD0", pNode1, 0, True, -1)
    Test("TestD1", pNode1, 1, False, 1)
    Test("TestD2", pNode1, 2, True, -1)

    #DestroyTree(pNode1)

    print("\n\n")


#// empty tree
def TestE():

    Test("TestE0", None, 0, True, -1)
    Test("TestE1", None, 1, True, -1)

    print("\n\n")


TestA()
TestB()
TestC()
TestD()
TestE()
    
