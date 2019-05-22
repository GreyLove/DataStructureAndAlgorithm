#2、两个二叉树的对应节点的数值合并，然后生成一个新的二叉树

class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def createNewTree(q,p):
    if q == None and p == None:
        return None
     
    if q == None:
        node = TreeNode(p.val)
    elif p == None:
        node = TreeNode(q.val)
    else:
        node = TreeNode(p.val+q.val)
    left1 = q.left if q != None else None
    left2 = p.left if p != None else None
    right1 = q.right if q != None else None
    right2 = p.right if p != None else None
    node.left = createNewTree(left1,left2)
    node.right= createNewTree(right1,right2)
    return node


def buildTree(preOrder,interOrder,start,end,index=[0]):
    if start > end:
        return None
    
    idx = index[0]
    val = preOrder[idx]
    node = TreeNode(val)
    for i in range(start,end+1):
        if interOrder[i] == val:
            break
    mid =  i
    index[0] += 1
    node.left = buildTree(preOrder,interOrder,start,mid-1,index)
    node.right = buildTree(preOrder,interOrder,mid+1,end,index)
    return node

pre = [4,2,1,3,6,5,8,9,7]
inter = [1,2,3,4,8,9,5,6,7]
root = buildTree(pre,inter,0,len(inter)-1,index=[0])

pre = [4,2,1,3,6,5,7,8]
inter = [1,2,3,4,5,6,7,8]
root1 = buildTree(pre,inter,0,len(inter)-1,index=[0])
print(root)

newRoot = createNewTree(root,root1)
print(newRoot)