

from MyTree import *

def maxPathTwoNode(root,left,right):
    if left == None or right == None:
        return []
    find1Path = []
    find2Path = []
    find1 = findPath(root,left,find1Path)
    find2 = findPath(root,right,find2Path)
    if not find1 or not find2:
        return
    i = 0
    same = True
    commonFather = None
    while i < len(find1Path) and i < len(find2Path):
        n1 = find1Path[i]
        n2 = find2Path[i]
        if n1 != n2:
            same = False
            commonFather = find1Path[i-1]
            break
        i += 1
    
    ll = []
    if same:
        if  len(find1Path) < len(find2Path):
            k = i-1
            while k<len(find2Path):
                ll.append(find2Path[k].val)
                k += 1
        else:
            k = i-1
            while k<len(find1Path):
                ll.append(find1Path[k].val)
                k += 1
    else:
        k = len(find1Path)-1
        while k>=0 and find1Path[k] != commonFather:
            ll.append(find1Path[k].val)
            k -= 1
        k = i-1
        while k<len(find2Path):
            ll.append(find2Path[k].val)
            k += 1

    return ll 


#//             1
#//         /      \
#//        2        3
#//       /\         \
#//      4  5         6
#//        /
#//       7

def findPath(root,node,path:list):
    if node == None or root == None:
        return False

    path.append(root)
    find = False
    if root == node:
        find = True
        return find

    if not find:
        find = findPath(root.left,node,path)
    
    if not find:
        find = findPath(root.right,node,path)
    
    if find:
        return True
    else:
        path.pop()
    
    return find

    

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

    node = maxPathTwoNode(pNode1,pNode1,pNode6)
    print(node)


Test2()