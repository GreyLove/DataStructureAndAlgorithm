class Graph(object):
    def __init__(self):
        self.v = 0 #顶点个数
        self.adj = [] #邻接表
    
    def Graph(self,v):
        self.v = v
        self.adj = [[] for _ in range(v)]
    
    def addEdge(self,s,t):
        self.adj[s].append(t)
        self.adj[t].append(s)
    
    def BFS(self):
        if self.v<=0:
            return
        visited = [False for _ in range(self.v)]
        queue = [0]
        visited[0] = True
        while len(queue):
            pop = queue.pop(0)
            print(pop)
            
            for i in range(len(self.adj[pop])):
                if visited[self.adj[pop][i]] == False:
                    queue.append(self.adj[pop][i])
                    visited[self.adj[pop][i]] = True
    
    def bfs(self,s,t):
        if self.v<=0:
            return
        if s<0 or s>=self.v or t<0 or t>self.v:
            return
        visited = [False for _ in range(self.v)]
        prevList = [-1 for _ in range(self.v)]
        queue = [s]
        visited[s] = True
        while len(queue):
            pop = queue.pop(0)
            print(pop)
            
            for i in range(len(self.adj[pop])):
                k = self.adj[pop][i]
                if visited[k] == False:
                    queue.append(k)
                    visited[k] = True
                    prevList[k] = pop

        print(prevList)
    
    def DFS(self):
        if self.v<=0:
            return
        visited = [False for _ in range(self.v)]
        prevList = [-1 for _ in range(self.v)]


        def dfsCore(visited,prevList):

            if visited

g = Graph()
g.Graph(8)
g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(1,2)
g.addEdge(1,4)
g.addEdge(3,4)
g.addEdge(2,5)
g.addEdge(4,5)
g.addEdge(4,6)
g.addEdge(5,7)
g.addEdge(6,7)

print(g)

# g.BFS()
g.bfs(0,6)