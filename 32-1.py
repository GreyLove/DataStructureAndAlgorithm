# // 面试题32（一）：不分行从上往下打印二叉树
# // 题目：从上往下打印出二叉树的每个结点，同一层的结点按照从左到右的顺序打印。


from MyTree import *

def PrintFromTopToBottom(root):
    if not root:
        return
    
    queue = [root]

    while len(queue):
        node = queue.pop(0)
        print(node.val)
        if node.left:queue.append(node.left)
        if node.right:queue.append(node.right)


# #// ====================辅助测试代码====================

def Test(testName, pRoot1, pRoot2, expected):
    print('----------%s---------' %(testName))
    PrintFromTopToBottom(pRoot1)


# #// 树中结点含有分叉，树B是树A的子结构
# #//                  8                8
# #//              /       \           / \
# #//             8         7         9   2
# #//           /   \
# #//          9     2
# #//               / \
# #//              4   7
def Test1():
    pNodeA1 = CreateBinaryTreeNode(8)
    pNodeA2 = CreateBinaryTreeNode(8)
    pNodeA3 = CreateBinaryTreeNode(7)
    pNodeA4 = CreateBinaryTreeNode(9)
    pNodeA5 = CreateBinaryTreeNode(2)
    pNodeA6 = CreateBinaryTreeNode(4)
    pNodeA7 = CreateBinaryTreeNode(7)

    ConnectTreeNodes(pNodeA1, pNodeA2, pNodeA3)
    ConnectTreeNodes(pNodeA2, pNodeA4, pNodeA5)
    ConnectTreeNodes(pNodeA5, pNodeA6, pNodeA7)

    pNodeB1 = CreateBinaryTreeNode(8)
    pNodeB2 = CreateBinaryTreeNode(9)
    pNodeB3 = CreateBinaryTreeNode(2)

    ConnectTreeNodes(pNodeB1, pNodeB2, pNodeB3)

    Test("Test1", pNodeA1, pNodeB1, True)




#// 树中结点含有分叉，树B不是树A的子结构
#//                  8                8
#//              /       \           / \
#//             8         7         9   2
#//           /   \
#//          9     3
#//               / \
#//              4   7
def Test2():

    pNodeA1 = CreateBinaryTreeNode(8)
    pNodeA2 = CreateBinaryTreeNode(8)
    pNodeA3 = CreateBinaryTreeNode(7)
    pNodeA4 = CreateBinaryTreeNode(9)
    pNodeA5 = CreateBinaryTreeNode(3)
    pNodeA6 = CreateBinaryTreeNode(4)
    pNodeA7 = CreateBinaryTreeNode(7)

    ConnectTreeNodes(pNodeA1, pNodeA2, pNodeA3)
    ConnectTreeNodes(pNodeA2, pNodeA4, pNodeA5)
    ConnectTreeNodes(pNodeA5, pNodeA6, pNodeA7)

    pNodeB1 = CreateBinaryTreeNode(8)
    pNodeB2 = CreateBinaryTreeNode(9)
    pNodeB3 = CreateBinaryTreeNode(2)

    ConnectTreeNodes(pNodeB1, pNodeB2, pNodeB3)

    Test("Test2", pNodeA1, pNodeB1, False)

    #DestroyTree(pNodeA1)
    #DestroyTree(pNodeB1)


#// 树中结点只有左子结点，树B是树A的子结构
#//                8                  8
#//              /                   / 
#//             8                   9   
#//           /                    /
#//          9                    2
#//         /      
#//        2        
#//       /
#//      5
def Test3():

    pNodeA1 = CreateBinaryTreeNode(8)
    pNodeA2 = CreateBinaryTreeNode(8)
    pNodeA3 = CreateBinaryTreeNode(9)
    pNodeA4 = CreateBinaryTreeNode(2)
    pNodeA5 = CreateBinaryTreeNode(5)

    ConnectTreeNodes(pNodeA1, pNodeA2, None)
    ConnectTreeNodes(pNodeA2, pNodeA3, None)
    ConnectTreeNodes(pNodeA3, pNodeA4, None)
    ConnectTreeNodes(pNodeA4, pNodeA5, None)

    pNodeB1 = CreateBinaryTreeNode(8)
    pNodeB2 = CreateBinaryTreeNode(9)
    pNodeB3 = CreateBinaryTreeNode(2)

    ConnectTreeNodes(pNodeB1, pNodeB2, None)
    ConnectTreeNodes(pNodeB2, pNodeB3, None)

    Test("Test3", pNodeA1, pNodeB1, True)

    #DestroyTree(pNodeA1)
    #DestroyTree(pNodeB1)


#// 树中结点只有左子结点，树B不是树A的子结构
#//                8                  8
#//              /                   / 
#//             8                   9   
#//           /                    /
#//          9                    3
#//         /      
#//        2        
#//       /
#//      5
def Test4():

    pNodeA1 = CreateBinaryTreeNode(8)
    pNodeA2 = CreateBinaryTreeNode(8)
    pNodeA3 = CreateBinaryTreeNode(9)
    pNodeA4 = CreateBinaryTreeNode(2)
    pNodeA5 = CreateBinaryTreeNode(5)

    ConnectTreeNodes(pNodeA1, pNodeA2, None)
    ConnectTreeNodes(pNodeA2, pNodeA3, None)
    ConnectTreeNodes(pNodeA3, pNodeA4, None)
    ConnectTreeNodes(pNodeA4, pNodeA5, None)

    pNodeB1 = CreateBinaryTreeNode(8)
    pNodeB2 = CreateBinaryTreeNode(9)
    pNodeB3 = CreateBinaryTreeNode(3)

    ConnectTreeNodes(pNodeB1, pNodeB2, None)
    ConnectTreeNodes(pNodeB2, pNodeB3, None)

    Test("Test4", pNodeA1, pNodeB1, False)

    #DestroyTree(pNodeA1)
    #DestroyTree(pNodeB1)


#// 树中结点只有右子结点，树B是树A的子结构
#//       8                   8
#//        \                   \ 
#//         8                   9   
#//          \                   \
#//           9                   2
#//            \      
#//             2        
#//              \
#//               5
def Test5():

    pNodeA1 = CreateBinaryTreeNode(8)
    pNodeA2 = CreateBinaryTreeNode(8)
    pNodeA3 = CreateBinaryTreeNode(9)
    pNodeA4 = CreateBinaryTreeNode(2)
    pNodeA5 = CreateBinaryTreeNode(5)

    ConnectTreeNodes(pNodeA1, None, pNodeA2)
    ConnectTreeNodes(pNodeA2, None, pNodeA3)
    ConnectTreeNodes(pNodeA3, None, pNodeA4)
    ConnectTreeNodes(pNodeA4, None, pNodeA5)

    pNodeB1 = CreateBinaryTreeNode(8)
    pNodeB2 = CreateBinaryTreeNode(9)
    pNodeB3 = CreateBinaryTreeNode(2)

    ConnectTreeNodes(pNodeB1, None, pNodeB2)
    ConnectTreeNodes(pNodeB2, None, pNodeB3)

    Test("Test5", pNodeA1, pNodeB1, True)

    #DestroyTree(pNodeA1)
    #DestroyTree(pNodeB1)


#// 树A中结点只有右子结点，树B不是树A的子结构
#//       8                   8
#//        \                   \ 
#//         8                   9   
#//          \                 / \
#//           9               3   2
#//            \      
#//             2        
#//              \
#//               5
def Test6():

    pNodeA1 = CreateBinaryTreeNode(8)
    pNodeA2 = CreateBinaryTreeNode(8)
    pNodeA3 = CreateBinaryTreeNode(9)
    pNodeA4 = CreateBinaryTreeNode(2)
    pNodeA5 = CreateBinaryTreeNode(5)

    ConnectTreeNodes(pNodeA1, None, pNodeA2)
    ConnectTreeNodes(pNodeA2, None, pNodeA3)
    ConnectTreeNodes(pNodeA3, None, pNodeA4)
    ConnectTreeNodes(pNodeA4, None, pNodeA5)

    pNodeB1 = CreateBinaryTreeNode(8)
    pNodeB2 = CreateBinaryTreeNode(9)
    pNodeB3 = CreateBinaryTreeNode(3)
    pNodeB4 = CreateBinaryTreeNode(2)

    ConnectTreeNodes(pNodeB1, None, pNodeB2)
    ConnectTreeNodes(pNodeB2, pNodeB3, pNodeB4)

    Test("Test6", pNodeA1, pNodeB1, False)

    #DestroyTree(pNodeA1)
    #DestroyTree(pNodeB1)


#// 树A为空树
def Test7():

    pNodeB1 = CreateBinaryTreeNode(8)
    pNodeB2 = CreateBinaryTreeNode(9)
    pNodeB3 = CreateBinaryTreeNode(3)
    pNodeB4 = CreateBinaryTreeNode(2)

    ConnectTreeNodes(pNodeB1, None, pNodeB2)
    ConnectTreeNodes(pNodeB2, pNodeB3, pNodeB4)

    Test("Test7", None, pNodeB1, False)

    #DestroyTree(pNodeB1)


#// 树B为空树
def Test8():

    pNodeA1 = CreateBinaryTreeNode(8)
    pNodeA2 = CreateBinaryTreeNode(9)
    pNodeA3 = CreateBinaryTreeNode(3)
    pNodeA4 = CreateBinaryTreeNode(2)

    ConnectTreeNodes(pNodeA1, None, pNodeA2)
    ConnectTreeNodes(pNodeA2, pNodeA3, pNodeA4)

    Test("Test8", pNodeA1, None, False)

    #DestroyTree(pNodeA1)


#// 树A和树B都为空
def Test9():

    Test("Test9", None, None, False)


Test1()
Test2()
Test3()
Test4()
Test5()
Test6()
Test7()
Test8()
Test9()
