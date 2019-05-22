# 1、找树的最长路径的两个节点

#根据前序和中序，生成一颗二叉树,数组中不能有重复数字
class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

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


def maxPath(root,path,pathList=[[]]):
    if not root:
        return
    path.append(root)
    if root.left == None and root.right == None:
        maxTmp = pathList[0]
        if len(path)>len(maxTmp):
            maxTmp.clear()
            for i in path:
                 maxTmp.append(i) 
    maxPath(root.left,path,pathList)
    maxPath(root.right,path,pathList)
    path.pop()



# pre = [4,2,1,3,6,5,7,8]
# inter = [1,2,3,4,5,6,7,8]

pre = [4,2,1,3,6,5,8,9,7]
inter = [1,2,3,4,8,9,5,6,7]

root = buildTree(pre,inter,0,len(inter)-1)
print(root)

path = [] 
pathList = [[]]
maxPath(root,path,pathList)
print(pathList[0])