# // 面试题7：重建二叉树
# // 题目：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输
# // 入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列
# {1, 2, 4, 7, 3, 5, 6, 8}和中序遍历序列{4, 7, 2, 1, 5, 3, 8, 6}，则重建出


class TreeNode(object):
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None


def Construct(preOrder,inOrder):
    if not preOrder or not inOrder or len(preOrder) != len(inOrder):
        return


    root = TreeNode(preOrder[0])
    i = 0
    for i in range(len(inOrder)):
        if root.val == inOrder[i]:
            break

    root.left = Construct(preOrder[1:i+1],inOrder[0:i])
    root.right = Construct(preOrder[i+1:],inOrder[i+1:])

    return root

def preOrderList(root,list = []):
    if root == None:
        return
    list.append(root.val)
    preOrderList(root.left,list)
    preOrderList(root.right,list)

def inOrderList(root,list = []):
    if root == None:
        return
    inOrderList(root.left,list)
    list.append(root.val)
    inOrderList(root.right,list)


def Test(preOrder,inOrder):

    head = Construct(preOrder,inOrder)

    preOrder1 = []
    preOrderList(head,preOrder1)

    inOrder1 = []
    inOrderList(head,inOrder1)

    print(preOrder1,inOrder1)
    
preOrder = [1,2,4,7,3,5,6,8]
inOrder = [4,7,2,1,5,3,8,6]
Test(preOrder,inOrder)

preOrder = [1,2,4,5,3,6,7]
inOrder = [4,2,5,1,6,3,7]
Test(preOrder,inOrder)

preOrder = [1,2,3,4]
inOrder = [4,3,2,1]
Test(preOrder,inOrder)
