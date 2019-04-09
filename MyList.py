class ListNode(object):
    def __init__(self, val):
        self.m_nValue = val
        self.m_pNext = None

def CreateListNode(value):
    return ListNode(value)

def PrintList(pNode):
    if(pNode == None):
    
        print("The node is None\n")
    
    else:
    
        print("The key in node is %d.\n"% pNode.m_nValue)

def PrintListNode(pNode):

    if(pNode == None):
    
        print("The node is None\n")
    
    else:
    
        print("The key in node is %d.\n"% pNode.m_nValue)

def ConnectListNodes(pCurrent, pNext):

    if(pCurrent == None):
    
        print("Error to connect two nodes.\n")
        
    pCurrent.m_pNext = pNext

def DestroyList(node):
    node = None