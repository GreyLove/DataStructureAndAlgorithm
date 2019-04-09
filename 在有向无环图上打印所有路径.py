def printPath(matrix,a,b,path):
    if matrix == None:
        return
    l = len(matrix)
    if a >=  l or b >= l:
        return

    path.append(a)
    if a == b:
        print(path)
        return
 
    sub = []
    for i in range(l):
        if matrix[a][i] > 0:
            sub.append(i)
    
    for i in sub:
        printPath(matrix,i,b,path)
        path.pop()
    

matrix = \
[[0,1,1,0,0],
[0,0,0,1,0],
[0,0,0,0,1],
[0,0,1,0,1],
[0,0,0,0,0]]

printPath(matrix,1,2,[])
