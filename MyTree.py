class BinaryTreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def CreateBinaryTreeNode(val):
    return BinaryTreeNode(val)

def ConnectTreeNodes(pParent, pLeft, pRight):
    if(pParent != None):
        pParent.left = pLeft
        pParent.right = pRight

def DestroyTree(root):
    pass