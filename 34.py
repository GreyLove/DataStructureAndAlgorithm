# #// 面试题34：二叉树中和为某一值的路径
# #// 题目：输入一棵二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所
# #// 有路径。从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

from MyTree import *

def FindPath(pRoot, expectedSum):
    if pRoot == None:
        return
    paths = []
    path = []
    FindCore(pRoot, expectedSum,[0],path,paths)
    for p in paths:
        print([node.val for node in p])
    

def FindCore(pRoot, expectedSum,s:list,path:list,paths:list)->list:
    if pRoot == None:
        return
    
    s[0] += pRoot.val
    path.append(pRoot)
    if s[0] == expectedSum and pRoot.left == None and pRoot.right == None:
        paths.append([node for node in path])
        path.pop()
        s[0] -= pRoot.val
        return
    elif s[0] > expectedSum:
        path.pop()
        s[0] -= pRoot.val
        return
        
    FindCore(pRoot.left,expectedSum,s,path,paths)
    FindCore(pRoot.right,expectedSum,s,path,paths)
    path.pop()
    s[0] -= pRoot.val


#// ====================测试代码====================
def Test(testName, pRoot,expectedSum):

    if(testName != None):
        print("%s begins:\n", testName)

    FindPath(pRoot, expectedSum)

    print("\n")


#//            10
#//         /      \
#//        5        12
#//       /\        
#//      4  7     
#// 有两条路径上的结点和为22
def Test1():

    pNode10 = CreateBinaryTreeNode(10)
    pNode5 = CreateBinaryTreeNode(5)
    pNode12 = CreateBinaryTreeNode(12)
    pNode4 = CreateBinaryTreeNode(4)
    pNode7 = CreateBinaryTreeNode(7)

    ConnectTreeNodes(pNode10, pNode5, pNode12)
    ConnectTreeNodes(pNode5, pNode4, pNode7)

    print("Two paths should be found in Test1.\n")
    Test("Test1", pNode10, 22)

    DestroyTree(pNode10)


#//            10
#//         /      \
#//        5        12
#//       /\        
#//      4  7     
#// 没有路径上的结点和为15
def Test2():

    pNode10 = CreateBinaryTreeNode(10)
    pNode5 = CreateBinaryTreeNode(5)
    pNode12 = CreateBinaryTreeNode(12)
    pNode4 = CreateBinaryTreeNode(4)
    pNode7 = CreateBinaryTreeNode(7)

    ConnectTreeNodes(pNode10, pNode5, pNode12)
    ConnectTreeNodes(pNode5, pNode4, pNode7)

    print("No paths should be found in Test2.\n")
    Test("Test2", pNode10, 15)

    DestroyTree(pNode10)


#//               5
#//              /
#//             4
#//            /
#//           3
#//          /
#//         2
#//        /
#//       1
#// 有一条路径上面的结点和为15
def Test3():

    pNode5 = CreateBinaryTreeNode(5)
    pNode4 = CreateBinaryTreeNode(4)
    pNode3 = CreateBinaryTreeNode(3)
    pNode2 = CreateBinaryTreeNode(2)
    pNode1 = CreateBinaryTreeNode(1)

    ConnectTreeNodes(pNode5, pNode4, None)
    ConnectTreeNodes(pNode4, pNode3, None)
    ConnectTreeNodes(pNode3, pNode2, None)
    ConnectTreeNodes(pNode2, pNode1, None)

    print("One path should be found in Test3.\n")
    Test("Test3", pNode5, 15)

    DestroyTree(pNode5)


#// 1
#//  \
#//   2
#//    \
#//     3
#//      \
#//       4
#//        \
#//         5
#// 没有路径上面的结点和为16
def Test4():

    pNode1 = CreateBinaryTreeNode(1)
    pNode2 = CreateBinaryTreeNode(2)
    pNode3 = CreateBinaryTreeNode(3)
    pNode4 = CreateBinaryTreeNode(4)
    pNode5 = CreateBinaryTreeNode(5)

    ConnectTreeNodes(pNode1, None, pNode2)
    ConnectTreeNodes(pNode2, None, pNode3)
    ConnectTreeNodes(pNode3, None, pNode4)
    ConnectTreeNodes(pNode4, None, pNode5)

    print("No paths should be found in Test4.\n")
    Test("Test4", pNode1, 16)

    DestroyTree(pNode1)


#// 树中只有1个结点
def Test5():

    pNode1 = CreateBinaryTreeNode(1)

    print("One path should be found in Test5.\n")
    Test("Test5", pNode1, 1)

    DestroyTree(pNode1)


#// 树中没有结点
def Test6():

    print("No paths should be found in Test6.\n")
    Test("Test6", None, 0)

Test1()
Test2()
Test3()
Test4()
Test5()
Test6()

