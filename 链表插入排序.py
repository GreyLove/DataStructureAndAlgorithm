class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

def insertSort(head):
    if head == None: 
        return
    
    head1 = head
    head2 = head.next
    cur1 = head1
    cur1.next = None
    cur2 = head2
    while cur2:
        pre = None
        while cur1 and cur2.val > cur1.val:
            pre = cur1
            cur1 = cur1.next
        head2 = cur2.next
        cur2.next = cur1
        if pre: 
            pre.next = cur2
        else:
            head1 = cur2
        cur1 = head1
        cur2 = head2
    return head1
                
def createList(s):
    if len(s) <= 0:
        return
    head = Node(s[0])
    cur = head
    for i in range(1,len(s)):
        cur.next = Node(s[i])
        cur = cur.next
    
    return head

k = [5,4,3,2,1]
k = [5,4,3,5,6]
k = [1,2,3,4,5]
k = [4,1,2,5,6]

head = createList(k)
print(head)
newHead = insertSort(head)
print(newHead)
                
             
            
            
            
