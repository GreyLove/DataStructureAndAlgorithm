class MySingleListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None

def connectListNodes(pCurrent, pNext):
    if(pCurrent == None):
        print("Error to connect two nodes.\n")
    pCurrent.next = pNext

class MySingleList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def insert(self,node):#O(1)
        if node == None:
            return False

        if self.tail:
            self.tail.next = node
            self.tail = self.tail.next
        else:
            self.head = node
            self.tail = node
        self.size += 1
        return True
    
    def delete(self,node):#O(1)
        if node == None:
            return False
        if node.next == None:
            cur = self.head
            while cur.next != node:
                cur = cur.next
            cur.next = None
            self.tail = cur
        else:
            node.val = node.next.val
            node.next = node.next.next
        self.size -= 1
        return True
    
    def print(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next
    


# li = MySingleList()
# node1 = MySingleListNode(1)
# node2 = MySingleListNode(2)
# node3 = MySingleListNode(3)

# li.insert(node1)
# li.insert(node2)
# li.insert(node3)

# li.print()

# li.delete(node3)

# li.print()

# print(li.size)