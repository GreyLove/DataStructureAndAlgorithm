
# 生成一颗二叉查找树

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def createBinaryTree(a):
    if not a:
        return
    return createCore(a,0,len(a)-1)


def createCore(a,i,j):
    if i > j:
        return
    if i == j:
        return TreeNode(a[i])
    
    m = (i+j)>>1

    root = TreeNode(a[m])

    root.left = createCore(a,i,m-1)
    root.right = createCore(a,m+1,j)

    return root

#    3
#1         5
#  2    4       6

root = createBinaryTree([1,2,3,4,5,6])

# 递归
def findNode(root,data):
    if not root:
        return None
    if root.val == data:
        return root
    elif root.val > data:
        return findNode(root.left,data)
    elif root.val < data:
        return findNode(root.right,data)
    
    return None

# 非递归
def findNodeNoReservse(root,data):
    if not data:
        return
    p = root

    while p:
        if p.val == data:
            return p
        elif p.val < data:
            p = p.right
        elif p.val > data:
            p = p.left
    
    return None

print(root)

data = 6
p1 = findNode(root,data)
p2 = findNodeNoReservse(root,data)

# if p1:
#     print(p1.val)

# if p2:
#     print(p2.val)

# 二叉搜索树，插入
def binaryInsert(root,data):
    
    p = root

    node = TreeNode(data)
    while p:
        
        if p.val < data:
            if not p.right:
                p.right = node
                return
            p = p.right
        else:
            if not p.left:
                p.left = node
                return
            p = p.left
    
    return node

# binaryInsert(root,1)


def binaryDelete(root,data):
    if not root:
        return
    
    cur = root
    parent = None
    while cur and cur.val != data:
        parent = cur
        if cur.val > data:
            cur = cur.left
        else:
            cur = cur.right
    
    if cur == None:return root# 没有找到
    # if parent == None:return None#删除的是根节点
    
    if cur.left and cur.right:
        p = cur.right
        pp = None
        while p.left:
            pp = p
            p = p.left
        
        cur.val = p.val
        if pp : pp.left = None
        else:cur.right = None
        return
    
    node = None
    if cur.left:node = cur.left
    elif cur.right:node = cur.right
    
    if parent == None:root = node
    elif parent.left == cur:parent.left = node
    else :parent.right == node

   
binaryDelete(root,5)


def binaryHeight(root):
    if root == None:
        return 0
    
    l = binaryHeight(root.left)+1
    r = binaryHeight(root.right)+1

    deep = max(l,r)
    return deep

binaryInsert(root,7)
# binaryInsert(root,8)
# binaryInsert(root,8)

h  = binaryHeight(root)

print(h)
end = 0