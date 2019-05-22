
class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

def BubbleSort(head):
    if head == None or head.next == None:
        return

    
    local = head
    while 1:
        flag = False
        pre = None
        cur = local
        nex = local.next
        while nex != None:
            if cur.val > nex.val:
                cur.next = nex.next
                nex.next = cur
                if pre == None:
                    local = nex
                else:
                    pre.next = nex
                pre = nex
                nex = cur.next
                flag = True
            else:
                if  pre == None:
                    local = cur
                pre = cur
                cur = nex
                nex = nex.next
        if not flag:
            return local
                 



k = 5
head = Node(k)
cur = head
k -= 1
while k > 0:
    cur.next = Node(k)
    k -= 1
    cur = cur.next

i = 0
head = Node(k)
cur = head
i += 1
while i <= 5:
    cur.next = Node(i)
    i += 1
    cur = cur.next

newHead = BubbleSort(head)

print(newHead)
