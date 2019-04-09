# #// 面试题55（一）：二叉树的深度
# #// 题目：输入一棵二叉树的根结点，求该树的深度。从根结点到叶结点依次经过的
# #// 结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

from MyTree import *

def TreeDepth(pRoot):
    if not pRoot:
        return 0
    l = TreeDepth(pRoot.left)+1
    r = TreeDepth(pRoot.right)+1
    
    return l if l > r else r




# #// ====================测试代码====================
def Test(testName, pRoot, expected):

    result = TreeDepth(pRoot)
    if(expected == result):
        print("%s passed.\n"% testName)
    else:
        print("%s FAILED.\n"% testName)


#//            1
#//         /      \
#//        2        3
#//       /\         \
#//      4  5         6
#//        /
#//       7
def Test1():

    pNode1 = CreateBinaryTreeNode(1)
    pNode2 = CreateBinaryTreeNode(2)
    pNode3 = CreateBinaryTreeNode(3)
    pNode4 = CreateBinaryTreeNode(4)
    pNode5 = CreateBinaryTreeNode(5)
    pNode6 = CreateBinaryTreeNode(6)
    pNode7 = CreateBinaryTreeNode(7)

    ConnectTreeNodes(pNode1, pNode2, pNode3)
    ConnectTreeNodes(pNode2, pNode4, pNode5)
    ConnectTreeNodes(pNode3, None, pNode6)
    ConnectTreeNodes(pNode5, pNode7, None)

    Test("Test1", pNode1, 4)

    #DestroyTree(pNode1)


#//               1
#//              /
#//             2
#//            /
#//           3
#//          /
#//         4
#//        /
#//       5
def Test2():

    pNode1 = CreateBinaryTreeNode(1)
    pNode2 = CreateBinaryTreeNode(2)
    pNode3 = CreateBinaryTreeNode(3)
    pNode4 = CreateBinaryTreeNode(4)
    pNode5 = CreateBinaryTreeNode(5)

    ConnectTreeNodes(pNode1, pNode2, None)
    ConnectTreeNodes(pNode2, pNode3, None)
    ConnectTreeNodes(pNode3, pNode4, None)
    ConnectTreeNodes(pNode4, pNode5, None)

    Test("Test2", pNode1, 5)

    #DestroyTree(pNode1)


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

    Test("Test3", pNode1, 5)

    #DestroyTree(pNode1)


#// 树中只有1个结点
def Test4():

    pNode1 = CreateBinaryTreeNode(1)
    Test("Test4", pNode1, 1)

    #DestroyTree(pNode1)


#// 树中没有结点
def Test5():

    Test("Test5", None, 0)



Test1()
Test2()
Test3()
Test4()
Test5()
