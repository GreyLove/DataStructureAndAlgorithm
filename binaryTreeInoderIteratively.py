class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        if not root:
            return
        
        cur = root
        stack = [root]
        l = []

        while len(stack):
            while cur:
                stack.append(cur.left)
                cur = cur.left
            
            pop  = stack.pop()
            if pop:
                l.append(pop.val)
                cur = pop.right

            if cur:
                stack.append(cur)

        return l
        

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)

n1.left = n2
n1.right = n3

n2.left = n5
n2.right = n6

l = Solution().inorderTraversal(n1)
print(l)