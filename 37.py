# // 面试题37：序列化二叉树
# // 题目：请实现两个函数，分别用来序列化和反序列化二叉树。

# // 面试题37：序列化二叉树
# // 题目：请实现两个函数，分别用来序列化和反序列化二叉树。

# 先序序列化
def Serialize(pNode1,serializeLis):
    if pNode1 == None:
        serializeLis.append("$")
        return

    serializeLis.append(pNode1.val)
    Serialize(pNode1.left,serializeLis)
    Serialize(pNode1.right,serializeLis)
    return serializeLis


def Deserialize(serializeLis,idx:list):
    if len(serializeLis) == 0:
        return
    if idx[0] >= len(serializeLis):
        return
    
    if serializeLis[idx[0]] != '$':
        val = serializeLis[idx[0]]
        node = BinaryTreeNode(val)
        idx[0] += 1
        node.left = Deserialize(serializeLis,idx)
        idx[0] += 1
        node.right = Deserialize(serializeLis,idx)
        return node

    


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


pNode10 = CreateBinaryTreeNode(10)
pNode6 = CreateBinaryTreeNode(6)
pNode14 = CreateBinaryTreeNode(14)
pNode4 = CreateBinaryTreeNode(4)
pNode8 = CreateBinaryTreeNode(8)
pNode12 = CreateBinaryTreeNode(12)
pNode16 = CreateBinaryTreeNode(16)

ConnectTreeNodes(pNode10, pNode6, pNode14)
ConnectTreeNodes(pNode6, pNode4, pNode8)
ConnectTreeNodes(pNode14, pNode12, pNode16)


# pNode5 = CreateBinaryTreeNode(5)
# pNode4 = CreateBinaryTreeNode(4)
# pNode3 = CreateBinaryTreeNode(3)
# pNode2 = CreateBinaryTreeNode(2)
# pNode1 = CreateBinaryTreeNode(1)

# ConnectTreeNodes(pNode5, pNode4, None)
# ConnectTreeNodes(pNode4, pNode3, None)
# ConnectTreeNodes(pNode3, pNode2, None)
# ConnectTreeNodes(pNode2, pNode1, None)



# pNode1 = CreateBinaryTreeNode(1)
# pNode2 = CreateBinaryTreeNode(2)
# pNode3 = CreateBinaryTreeNode(3)
# pNode4 = CreateBinaryTreeNode(4)
# pNode5 = CreateBinaryTreeNode(5)

# ConnectTreeNodes(pNode1, None, pNode2)
# ConnectTreeNodes(pNode2, None, pNode3)
# ConnectTreeNodes(pNode3, None, pNode4)
# ConnectTreeNodes(pNode4, None, pNode5)

serializeLis = Serialize(pNode10,[])
print(serializeLis)


root = Deserialize(serializeLis,[0])
print(root)
