class Graph:
    def __init__(self,vertexs):
        n = len(vertexs)
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]
    def addEdge(self,fo,to,degree=1):
        self.matrix[fo][to] = degree

vertexs = ['a','b','c','d','e','f']
g = Graph(vertexs)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(2,4)
g.addEdge(3,0)
g.addEdge(3,1)
g.addEdge(4,3)
g.addEdge(5,4)
g.addEdge(5,2)
g.addEdge(5,3)
g.addEdge(2,5)
print(g.matrix)