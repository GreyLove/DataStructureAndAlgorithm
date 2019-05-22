from MySingleList import *


def CheckReseverse(head):
    if head == None or head.next == None:
        return head
    
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    nextP = None
    cur = head
    preP = head.next

    while cur != slow:
        cur.next = nextP
        nextP = cur
        cur = preP
        preP = preP.next
    
    head1 = nextP
    head2 = slow if not fast else slow.next

    cur1 = head1
    cur2 = head2

    success = True
    while cur1 and cur2:
        if cur1.val != cur2.val:
            success = False
        cur1 = cur1.next
        cur2 = cur2.next
    
    #还原链表
    nextP = None
    cur = head1
    preP = head1.next

    while cur != None:
        cur.next = nextP
        nextP = cur
        cur = preP
        preP = preP if preP == None else preP.next
    
    nextP.next = slow
    
    return success

if __name__ == "__main__":
    a = MySingleListNode('a')
    b = MySingleListNode('b')

    a1 = MySingleListNode('a')
    b1 = MySingleListNode('b')

    connectListNodes(a,b)
    # connectListNodes(b,a1)
    # connectListNodes(b1,a1)

    n = CheckReseverse(a)
    print(n)
    



