# #// 面试题55（二）：平衡二叉树
# #// 题目：输入一棵二叉树的根结点，判断该树是不是平衡二叉树。如果某二叉树中
# #// 任意结点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

from MyTree import *

def IsBalanced_Solution(pRoot,deep):
    if not pRoot:
        return True
    
    deep_l = [0]
    balance_l = IsBalanced_Solution(pRoot.left,deep_l)
    deep_l[0] += 1

    deep_r = [0]
    balance_r = IsBalanced_Solution(pRoot.right,deep_r)
    deep_r[0] += 1

    diff = deep_l[0] - deep_r[0]
    if balance_l and balance_r and  diff >= -1 and diff <= 1:
        deep[0] = deep_l[0] if deep_l[0] > deep_r[0] else deep_r[0]
        return True

    
    return False





#// ====================测试代码====================
def Test(testName, pRoot, expected):

    if(testName != None):
        print("%s begins:\n", testName)

    print("Solution1 begins: ")
    if(IsBalanced_Solution(pRoot,[0]) == expected):
        print("Passed.\n")
    else:
        print("Failed.\n")


#// 完全二叉树
#//             1
#//         /      \
#//        2        3
#//       /\       / \
#//      4  5     6   7
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
    ConnectTreeNodes(pNode3, pNode6, pNode7)

    Test("Test1", pNode1, True)

    #DestroyTree(pNode1)


#// 不是完全二叉树，但是平衡二叉树
#//             1
#//         /      \
#//        2        3
#//       /\         \
#//      4  5         6
#//        /
#//       7
def Test2():

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

    Test("Test2", pNode1, True)

    #DestroyTree(pNode1)


#// 不是平衡二叉树
#//             1
#//         /      \
#//        2        3
#//       /\         
#//      4  5        
#//        /
#//       6
def Test3():

    pNode1 = CreateBinaryTreeNode(1)
    pNode2 = CreateBinaryTreeNode(2)
    pNode3 = CreateBinaryTreeNode(3)
    pNode4 = CreateBinaryTreeNode(4)
    pNode5 = CreateBinaryTreeNode(5)
    pNode6 = CreateBinaryTreeNode(6)

    ConnectTreeNodes(pNode1, pNode2, pNode3)
    ConnectTreeNodes(pNode2, pNode4, pNode5)
    ConnectTreeNodes(pNode5, pNode6, None)

    Test("Test3", pNode1, False)

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
def Test4():

    pNode1 = CreateBinaryTreeNode(1)
    pNode2 = CreateBinaryTreeNode(2)
    pNode3 = CreateBinaryTreeNode(3)
    pNode4 = CreateBinaryTreeNode(4)
    pNode5 = CreateBinaryTreeNode(5)

    ConnectTreeNodes(pNode1, pNode2, None)
    ConnectTreeNodes(pNode2, pNode3, None)
    ConnectTreeNodes(pNode3, pNode4, None)
    ConnectTreeNodes(pNode4, pNode5, None)

    Test("Test4", pNode1, False)

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
def Test5():

    pNode1 = CreateBinaryTreeNode(1)
    pNode2 = CreateBinaryTreeNode(2)
    pNode3 = CreateBinaryTreeNode(3)
    pNode4 = CreateBinaryTreeNode(4)
    pNode5 = CreateBinaryTreeNode(5)

    ConnectTreeNodes(pNode1, None, pNode2)
    ConnectTreeNodes(pNode2, None, pNode3)
    ConnectTreeNodes(pNode3, None, pNode4)
    ConnectTreeNodes(pNode4, None, pNode5)

    Test("Test5", pNode1, False)

    #DestroyTree(pNode1)


#// 树中只有1个结点
def Test6():

    pNode1 = CreateBinaryTreeNode(1)
    Test("Test6", pNode1, True)

    #DestroyTree(pNode1)


#// 树中没有结点
def Test7():

    Test("Test7", None, True)



Test1()
Test2()
Test3()
Test4()
Test5()
Test6()
Test7()

