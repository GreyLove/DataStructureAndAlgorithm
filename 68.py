# #// 面试题68：树中两个结点的最低公共祖先
# #// 题目：输入两个树结点，求它们的最低公共祖先。


class TreeNode(object):
    def __init__(self,val):
        self.m_nValue = val
        self.m_vChildren = []

def CreateTreeNode(val):
    return TreeNode(val)

def ConnectTreeNodes(pParent, pChild):

    if(pParent != None):
        pParent.m_vChildren.append(pChild)


def GetLastCommonParent(pRoot, pNode1, pNode2):
    path1 = []
    path2 = []
    find1 = findPath(pRoot, pNode1,path1)
    find2 = findPath(pRoot, pNode2,path2)

    if not find1 or not find2:
        return None
    
    i = 0
    j = 0
    while i<len(path1) and j<len(path2):
        p1 = path1[i]
        p2 = path2[j]
        if p1 != p2:
            return path1[i-1]
        i += 1
        j += 1
    
    if i == len(path1):
        return  path1[i-2]
    elif j == len(path2):
        return path2[j-2]
        

def findPath(pRoot,pNode,path:list)->bool:
    if not pRoot:
        return False

    path.append(pRoot)
    if pRoot == pNode:
        return True

    find = False
    for c in pRoot.m_vChildren:
        find = findPath(c,pNode,path)
        if find:
            break
    if not find:
        path.pop()
    return find





#// ====================测试代码====================
def Test(testName,  pRoot,  pNode1,  pNode2, pExpected):

    if(testName != None):
        print("%s begins: "% testName)

    pResult = GetLastCommonParent(pRoot, pNode1, pNode2)

    if((pExpected == None and pResult == None) or \
        (pExpected != None and pResult != None and pResult.m_nValue == pExpected.m_nValue)):
        print("Passed.\n")
    else:
        print("Failed.\n")


#// 形状普通的树
#//              1
#//            /   \
#//           2     3
#//       /       \
#//      4         5
#//     / \      / |  \
#//    6   7    8  9  10
def Test1():

    pNode1 = CreateTreeNode(1)
    pNode2 = CreateTreeNode(2)
    pNode3 = CreateTreeNode(3)
    pNode4 = CreateTreeNode(4)
    pNode5 = CreateTreeNode(5)
    pNode6 = CreateTreeNode(6)
    pNode7 = CreateTreeNode(7)
    pNode8 = CreateTreeNode(8)
    pNode9 = CreateTreeNode(9)
    pNode10 = CreateTreeNode(10)

    ConnectTreeNodes(pNode1, pNode2)
    ConnectTreeNodes(pNode1, pNode3)

    ConnectTreeNodes(pNode2, pNode4)
    ConnectTreeNodes(pNode2, pNode5)

    ConnectTreeNodes(pNode4, pNode6)
    ConnectTreeNodes(pNode4, pNode7)

    ConnectTreeNodes(pNode5, pNode8)
    ConnectTreeNodes(pNode5, pNode9)
    ConnectTreeNodes(pNode5, pNode10)

    Test("Test1", pNode1, pNode6, pNode8, pNode2)


#// 树退化成一个链表
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

    pNode1 = CreateTreeNode(1)
    pNode2 = CreateTreeNode(2)
    pNode3 = CreateTreeNode(3)
    pNode4 = CreateTreeNode(4)
    pNode5 = CreateTreeNode(5)

    ConnectTreeNodes(pNode1, pNode2)
    ConnectTreeNodes(pNode2, pNode3)
    ConnectTreeNodes(pNode3, pNode4)
    ConnectTreeNodes(pNode4, pNode5)

    Test("Test2", pNode1, pNode5, pNode4, pNode3)


#// 树退化成一个链表，一个结点不在树中
#//               1
#//              /
#//             2
#//            /
#//           3
#//          /
#//         4
#//        /
#//       5
def Test3():

    pNode1 = CreateTreeNode(1)
    pNode2 = CreateTreeNode(2)
    pNode3 = CreateTreeNode(3)
    pNode4 = CreateTreeNode(4)
    pNode5 = CreateTreeNode(5)

    ConnectTreeNodes(pNode1, pNode2)
    ConnectTreeNodes(pNode2, pNode3)
    ConnectTreeNodes(pNode3, pNode4)
    ConnectTreeNodes(pNode4, pNode5)

    pNode6 = CreateTreeNode(6)

    Test("Test3", pNode1, pNode5, pNode6, None)


#// 输入None
def Test4():

    Test("Test4", None, None, None, None)


Test1()
Test2()
Test3()
Test4()
