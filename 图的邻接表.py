
class vertex:
        def __init__(self,v,degree):
            self.v = v
            self.degree = degree

class Graph:# 基本上是对于无权图写的
            
    def __init__(self):
        self.m = {}
        self.first = None

    def addEdge(self,fo,to,degree=1):
        if self.first == None:
            self.first = fo
        v = vertex(to,degree)
        if fo in self.m:
            arr = self.m[fo]
            arr.append(v)
        else:
            self.m[fo] = []
            self.m[fo].append(v) 
    
    def bfs(self):

        if len(self.m) <= 0:
            return
        
        queue = [self.first]
        visited = set()
        visited.add(self.first)
        while len(queue):
            p = queue.pop(0)
            print(p)
            a = self.m[p] if p in self.m else []
            for v in a:
                if v.v not in visited:
                    queue.append(v.v)
                    visited.add(v.v)
    
    def dfs(self,fo,visited=set()):
        if len(self.m) <= 0:
            return
        if fo in visited:
            return
        visited.add(fo)
        print(fo)
        a = self.m[fo] if fo in self.m else []
        for v in a:
            self.dfs(v.v,visited)
    
    # 无权图的查找最短路径
    def findMinPath(self,s,t):
        if len(self.m) <= 0:
            return
        
        queue = [s]
        visited = set()
        visited.add(s)
        prev = {s:None}
        while len(queue):
            p = queue.pop(0)
            a = self.m[p] if p in self.m else []
            for v in a:
                if v.v not in visited:
                    queue.append(v.v)
                    prev[v.v] = p
                    visited.add(v.v)
                    if v.v == t:
                        stack = [v.v]
                        while prev[stack[-1]]:
                            stack.append(prev[stack[-1]])
                        # stack.append(t)
                        while len(stack):
                            k = stack.pop()
                            print(k)
                        return
        


g = Graph()
g.addEdge('a','c')
g.addEdge('a','b')
g.addEdge('c','e')
g.addEdge('c','f')
g.addEdge('d','a')
g.addEdge('d','b')
g.addEdge('e','d')
g.addEdge('f','e')
g.addEdge('f','c')
g.addEdge('f','d')

print(g.m)

g.bfs()
print('---------')
g.dfs('a')
print('---------')

g.findMinPath('a','f')