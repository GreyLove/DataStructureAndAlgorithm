class TrieNode():
    def __init__(self,v):
        self.v = v
        self.childs = {}

class Trie(object):
    def __init__(self):
        self.head = TrieNode('/')

    def insert(self,s):
        if not s:
            return
        p = self.head
        for i in s:
            if i in p.childs:
                p = p.childs[i]
                continue
            else:
                node = TrieNode(i)
                p.childs[i] = node
                p = node

    def find(self,s):

        if not s :
            return

        p = self.head
        for i in s:
            if i in p.childs:
                p = p.childs[i]
            else:
                return -1

        return 1

trie = Trie()
arr = ['hello','he','her','real']
for i in arr:
    trie.insert(i)
for i in arr:
    b = trie.find('22')
    print(b)
pass

        
        