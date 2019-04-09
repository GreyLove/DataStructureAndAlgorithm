# #// 面试题28：对称的二叉树
# #// 题目：请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和
# #// 它的镜像一样，那么它是对称的。
from MyTree import *

def isSymmetrical(pRoot):
    if pRoot == None:return True
    return isSymmetricalCore(pRoot.left,pRoot.right)

def isSymmetricalCore(a,b):
    if a == None and b == None:
        return True
    elif a == None or b == None:
        return False
    
    if a.val == b.val:
        return isSymmetricalCore(a.left,b.right) and \
            isSymmetricalCore(a.right,b.left)
    
    return False


def Test(testName,pRoot,expected):

    if(testName != None):
        print("%s begins: ", testName)

    if(isSymmetrical(pRoot) == expected):
        print("Passed.\n")
    else:
        print("FAILED.\n")


#//            8
#//        6      6
#//       5 7    7 5
def Test1():

    pNode8 = CreateBinaryTreeNode(8)
    pNode61 = CreateBinaryTreeNode(6)
    pNode62 = CreateBinaryTreeNode(6)
    pNode51 = CreateBinaryTreeNode(5)
    pNode71 = CreateBinaryTreeNode(7)
    pNode72 = CreateBinaryTreeNode(7)
    pNode52 = CreateBinaryTreeNode(5)

    ConnectTreeNodes(pNode8, pNode61, pNode62)
    ConnectTreeNodes(pNode61, pNode51, pNode71)
    ConnectTreeNodes(pNode62, pNode72, pNode52)

    Test("Test1", pNode8, True)

    #DestroyTree(pNode8)


#//            8
#//        6      9
#//       5 7    7 5
def Test2():

    pNode8 = CreateBinaryTreeNode(8)
    pNode61 = CreateBinaryTreeNode(6)
    pNode9 = CreateBinaryTreeNode(9)
    pNode51 = CreateBinaryTreeNode(5)
    pNode71 = CreateBinaryTreeNode(7)
    pNode72 = CreateBinaryTreeNode(7)
    pNode52 = CreateBinaryTreeNode(5)

    ConnectTreeNodes(pNode8, pNode61, pNode9)
    ConnectTreeNodes(pNode61, pNode51, pNode71)
    ConnectTreeNodes(pNode9, pNode72, pNode52)

    Test("Test2", pNode8, False)

    #DestroyTree(pNode8)


#//            8
#//        6      6
#//       5 7    7
def Test3():

    pNode8 = CreateBinaryTreeNode(8)
    pNode61 = CreateBinaryTreeNode(6)
    pNode62 = CreateBinaryTreeNode(6)
    pNode51 = CreateBinaryTreeNode(5)
    pNode71 = CreateBinaryTreeNode(7)
    pNode72 = CreateBinaryTreeNode(7)

    ConnectTreeNodes(pNode8, pNode61, pNode62)
    ConnectTreeNodes(pNode61, pNode51, pNode71)
    ConnectTreeNodes(pNode62, pNode72, None)

    Test("Test3", pNode8, False)

    #DestroyTree(pNode8)


#//               5
#//              / \
#//             3   3
#//            /     \
#//           4       4
#//          /         \
#//         2           2
#//        /             \
#//       1               1
def Test4():

    pNode5 = CreateBinaryTreeNode(5)
    pNode31 = CreateBinaryTreeNode(3)
    pNode32 = CreateBinaryTreeNode(3)
    pNode41 = CreateBinaryTreeNode(4)
    pNode42 = CreateBinaryTreeNode(4)
    pNode21 = CreateBinaryTreeNode(2)
    pNode22 = CreateBinaryTreeNode(2)
    pNode11 = CreateBinaryTreeNode(1)
    pNode12 = CreateBinaryTreeNode(1)

    ConnectTreeNodes(pNode5, pNode31, pNode32)
    ConnectTreeNodes(pNode31, pNode41, None)
    ConnectTreeNodes(pNode32, None, pNode42)
    ConnectTreeNodes(pNode41, pNode21, None)
    ConnectTreeNodes(pNode42, None, pNode22)
    ConnectTreeNodes(pNode21, pNode11, None)
    ConnectTreeNodes(pNode22, None, pNode12)

    Test("Test4", pNode5, True)

    #DestroyTree(pNode5)



#//               5
#//              / \
#//             3   3
#//            /     \
#//           4       4
#//          /         \
#//         6           2
#//        /             \
#//       1               1
def Test5():

    pNode5 = CreateBinaryTreeNode(5)
    pNode31 = CreateBinaryTreeNode(3)
    pNode32 = CreateBinaryTreeNode(3)
    pNode41 = CreateBinaryTreeNode(4)
    pNode42 = CreateBinaryTreeNode(4)
    pNode6 = CreateBinaryTreeNode(6)
    pNode22 = CreateBinaryTreeNode(2)
    pNode11 = CreateBinaryTreeNode(1)
    pNode12 = CreateBinaryTreeNode(1)

    ConnectTreeNodes(pNode5, pNode31, pNode32)
    ConnectTreeNodes(pNode31, pNode41, None)
    ConnectTreeNodes(pNode32, None, pNode42)
    ConnectTreeNodes(pNode41, pNode6, None)
    ConnectTreeNodes(pNode42, None, pNode22)
    ConnectTreeNodes(pNode6, pNode11, None)
    ConnectTreeNodes(pNode22, None, pNode12)

    Test("Test5", pNode5, False)

    #DestroyTree(pNode5)


#//               5
#//              / \
#//             3   3
#//            /     \
#//           4       4
#//          /         \
#//         2           2
#//                      \
#//                       1
def Test6():

    pNode5 = CreateBinaryTreeNode(5)
    pNode31 = CreateBinaryTreeNode(3)
    pNode32 = CreateBinaryTreeNode(3)
    pNode41 = CreateBinaryTreeNode(4)
    pNode42 = CreateBinaryTreeNode(4)
    pNode21 = CreateBinaryTreeNode(2)
    pNode22 = CreateBinaryTreeNode(2)
    pNode12 = CreateBinaryTreeNode(1)

    ConnectTreeNodes(pNode5, pNode31, pNode32)
    ConnectTreeNodes(pNode31, pNode41, None)
    ConnectTreeNodes(pNode32, None, pNode42)
    ConnectTreeNodes(pNode41, pNode21, None)
    ConnectTreeNodes(pNode42, None, pNode22)
    ConnectTreeNodes(pNode21, None, None)
    ConnectTreeNodes(pNode22, None, pNode12)

    Test("Test6", pNode5, False)

    #DestroyTree(pNode5)


#// 只有一个结点
def Test7():

    pNode1 = CreateBinaryTreeNode(1)
    Test("Test7", pNode1, True)

    #DestroyTree(pNode1)


#// 没有结点
def Test8():

    Test("Test8", None, True)


#// 所有结点都有相同的值，树对称
#//               5
#//              / \
#//             5   5
#//            /     \
#//           5       5
#//          /         \
#//         5           5
def Test9():

    pNode1 = CreateBinaryTreeNode(5)
    pNode21 = CreateBinaryTreeNode(5)
    pNode22 = CreateBinaryTreeNode(5)
    pNode31 = CreateBinaryTreeNode(5)
    pNode32 = CreateBinaryTreeNode(5)
    pNode41 = CreateBinaryTreeNode(5)
    pNode42 = CreateBinaryTreeNode(5)

    ConnectTreeNodes(pNode1, pNode21, pNode22)
    ConnectTreeNodes(pNode21, pNode31, None)
    ConnectTreeNodes(pNode22, None, pNode32)
    ConnectTreeNodes(pNode31, pNode41, None)
    ConnectTreeNodes(pNode32, None, pNode42)
    ConnectTreeNodes(pNode41, None, None)
    ConnectTreeNodes(pNode42, None, None)

    Test("Test9", pNode1, True)

    #DestroyTree(pNode1)


#// 所有结点都有相同的值，树不对称
#//               5
#//              / \
#//             5   5
#//            /     \
#//           5       5
#//          /       /
#//         5       5
def Test10():

    pNode1 = CreateBinaryTreeNode(5)
    pNode21 = CreateBinaryTreeNode(5)
    pNode22 = CreateBinaryTreeNode(5)
    pNode31 = CreateBinaryTreeNode(5)
    pNode32 = CreateBinaryTreeNode(5)
    pNode41 = CreateBinaryTreeNode(5)
    pNode42 = CreateBinaryTreeNode(5)

    ConnectTreeNodes(pNode1, pNode21, pNode22)
    ConnectTreeNodes(pNode21, pNode31, None)
    ConnectTreeNodes(pNode22, None, pNode32)
    ConnectTreeNodes(pNode31, pNode41, None)
    ConnectTreeNodes(pNode32, pNode42, None)
    ConnectTreeNodes(pNode41, None, None)
    ConnectTreeNodes(pNode42, None, None)

    Test("Test10", pNode1, False)

    #DestroyTree(pNode1)


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
