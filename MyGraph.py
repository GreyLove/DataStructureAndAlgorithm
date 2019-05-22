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
    
    def addEdge1(self,s,t):
        self.adj[s].append(t)
    
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
        def printList(prevList,t,path):
            if t == -1:
                return
            prev = prevList[t]
            printList(prevList,prev,path)
            path.append(t)
        visited = [False for _ in range(self.v)]
        prevList = [-1 for _ in range(self.v)]
        queue = [s]
        visited[s] = True
        while len(queue):
            pop = queue.pop(0)
            # print(pop)
            
            for i in range(len(self.adj[pop])):
                k = self.adj[pop][i]
                if visited[k] == False:
                    queue.append(k)
                    visited[k] = True
                    prevList[k] = pop
                    if k == t:
                        path = []
                        printList(prevList,t,path)
                        print(path)



        # print(prevList)
    
    def DFS(self):
        if self.v<=0:
            return
        
        visited = [False for _ in range(self.v)]
            
        def dfsCore(visited,adj,index):
            if visited[index] == True:return
            print(index)
            visited[index] = True
            a = adj[index]
            for i in range(len(a)):
                dfsCore(visited,adj,a[i])
        dfsCore(visited,self.adj,0)
    
    def dfs(self,s,t):
        if self.v<=0:
            return
        if s<0 or s>=self.v or t<0 or t>self.v:
            return
        visited = [False for _ in range(self.v)]
            
        def dfsCore(visited,adj,index,t,path):
            if visited[index] == True:return
            # print(index)
            path.append(index)
            visited[index] = True
            if index == t:
                print(path)
                
            a = adj[index]
            for i in range(len(a)):
                dfsCore(visited,adj,a[i],t,path)
            path.pop()
            visited[index] = False

        dfsCore(visited,self.adj,s,t,[])
    
    def topoSortByKahn(self):
        if self.v<=0:
            return
        inDegree = [0 for _ in range(self.v)]
        for i in range(self.v):
            for j in range(len(self.adj[i])):
                inDegree[self.adj[i][j]] += 1
        
        queue = []
        for i in range(self.v):
            if inDegree[i] == 0:
                queue.append(i)
        
        while len(queue)>0:
            pop = queue.pop(0)
            print("->",pop)
            a = self.adj[pop]
            for i in range(len(a)):
                inDegree[a[i]] -= 1
                if inDegree[a[i]] == 0:
                    queue.append(a[i])
                    
            
        


# g = Graph()
# g.Graph(8)
# g.addEdge(0,1)
# g.addEdge(0,3)
# g.addEdge(1,2)
# g.addEdge(1,4)
# g.addEdge(3,4)
# g.addEdge(2,5)
# g.addEdge(4,5)
# g.addEdge(4,6)
# g.addEdge(5,7)
# g.addEdge(6,7)

g = Graph()
g.Graph(8)
g.addEdge1(0,1)
g.addEdge1(0,3)
g.addEdge1(1,2)
g.addEdge1(1,4)
g.addEdge1(3,4)
g.addEdge1(2,5)
g.addEdge1(4,5)
g.addEdge1(4,6)
g.addEdge1(5,7)
g.addEdge1(6,7)
g.topoSortByKahn()

# print(g)

# g.BFS()
# g.bfs(0,7)
# print('============')
# g.DFS()
# g.dfs(0,7)