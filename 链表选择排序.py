class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

def createList(s):
    if len(s) <= 0:
        return
    head = Node(s[0])
    cur = head
    for i in range(1,len(s)):
        cur.next = Node(s[i])
        cur = cur.next
    return head

def SelectSort(head):
    if not head:
        return
    newHead = None
    newHeadCur = None
    cur = head
    minNode = head
    while cur:
        
        pre = None
        preMin = None
        while cur:
            if minNode.val > cur.val:
                preMin = pre
                minNode = cur
            pre = cur
            cur = cur.next
        if preMin == None:
            head = head.next
        else:
            preMin.next = minNode.next
        if newHead == None:
            newHead = minNode
            newHeadCur = newHead
        else:
            newHeadCur.next = minNode
            newHeadCur = newHeadCur.next
        cur = head
        minNode = head
        
    return newHead
    
k = [1]
# k = [2,1]
# k = [5,4,3,2,1]
# k = [5,4,3,5,6]
# k = [1,2,3,4,5]
# k = [4,1,2,0,6]

head = createList(k)
newHead = SelectSort(head)
print(newHead)
