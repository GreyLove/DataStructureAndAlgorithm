# // 面试题12：矩阵中的路径
# // 题目：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有
# // 字符的路径。路径可以从矩阵中任意一格开始，每一步可以在矩阵中向左、右、
# // 上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入
# // 该格子。例如在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字
# // 母用下划线标出）。但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个
# // 字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
# // A B T G
# // C F C S
# // J D E H

def findPath(matrix,path):
    if not matrix or len(matrix) == 0 or not path or len(path) == 0:
        return
    
    row = len(matrix)
    col = len(matrix[0])

    visited = [[False for _ in range(col)] for _ in range(row)]

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == path[0]:
                find = findPathCore(matrix,path,visited,row,col,i,j,[0])
                return find

def findPathCore(matrix,path,visited,row,col,i,j,index):
    if i > row-1 or i < 0 or j > col-1 or j < 0 or visited[i][j]:
        return False

    if index[0] == len(path):
        return True
     
    if matrix[i][j] ==  path[index[0]]:
        index[0] += 1
        visited[i][j] = True

        find =  findPathCore(matrix,path,visited,row,col,i-1,j,index) or \
                findPathCore(matrix,path,visited,row,col,i+1,j,index) or \
                findPathCore(matrix,path,visited,row,col,i,j-1,index) or \
                findPathCore(matrix,path,visited,row,col,i,j+1,index)
        
        if not find:
            visited[i][j] = False
            index[0] -= 1
        else:
            return True
    
    return False




matrix = "ABTGCFCSJDEH"
k = 0
row = 3
col = 4
lists = []
for i in range(row):
    list = []
    for j in range(col):
        list.append(matrix[k])
        k += 1
    
    lists.append(list)
# path = "ACFB"
# path = "HECS"
# path = "HEDJM"
path = "ABFB"

find = findPath(lists,path)
print(find)
