# // 面试题32（三）：之字形打印二叉树
# // 题目：请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺
# // 序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，
# // 其他行以此类推。

from MyTree import *

def printBinaryTreeNode(root):
    if root == None:
        return
    
    stack1 = [root]
    stack2 = []

    while len(stack1) or len(stack2):
        if len(stack1):
            print([node.val for node in stack1])
            while len(stack1):
                node = stack1.pop(0)
                if node.right:
                    stack2.append(node.right)
                if node.left:
                    stack2.append(node.left)
        else:
            print([node.val for node in stack2])
            while len(stack2):
                node = stack2.pop()
                if node.left:
                    stack1.append(node.left)
                if node.right:
                    stack1.append(node.right)



def Test(testName, pRoot1, pRoot2, expected):
    print('----------%s---------' %(testName))
    printBinaryTreeNode(pRoot1)


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