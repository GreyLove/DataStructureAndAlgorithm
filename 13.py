# // 面试题13：机器人的运动范围
# // 题目：地上有一个m行n列的方格。一个机器人从坐标(0, 0)的格子开始移动，它
# // 每一次可以向左、右、上、下移动一格，但不能进入行坐标和列坐标的数位之和
# // 大于k的格子。例如，当k为18时，机器人能够进入方格(35, 37)，因为3+5+3+7=18。
# // 但它不能进入方格(35, 38)，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

def movingCount(threshold,row,col):
    if row <= 0 or col <= 0:
        return 0
    visited = [[False for _ in range(col)] for _ in range(row)]
    count = movingCountCore(threshold,row,col,0,0,visited)
    return count

def movingCountCore(threshold,row,col,i,j,visited):
    if i < 0 or i > row-1 or j < 0 or j > col-1 or visited[i][j]:
        return 0
    
    count = 0
    if threshold >= constraint(i,j):
        visited[i][j] = True        
        count = movingCountCore(threshold,row,col,i-1,j,visited) +  \
                movingCountCore(threshold,row,col,i+1,j,visited) +  \
                movingCountCore(threshold,row,col,i,j-1,visited) +  \
                movingCountCore(threshold,row,col,i,j+1,visited) + 1

    return count

def constraint(i,j):
    s = 0
    while i > 0:
        s += i%10
        i = int(i/10)
    while j > 0:
        s += j%10
        j = int(j/10)
    return s

# // ====================测试代码====================
def test( testName,  threshold,  rows,  cols,  expected):

    if(testName != None):
        print("%s begins: " % (testName))
    l = movingCount(threshold, rows, cols)
    # print(l,'----',expected)
    if (l == expected):
        print("Passed.")
    else:
        print("FAILED.")

# // 方格多行多列
def test1():
    test("Test1", 5, 10, 10, 21)

# // 方格多行多列
def test2():
    test("Test2", 15, 20, 20, 359)

# // 方格只有一行，机器人只能到达部分方格
def test3():
    test("Test3", 10, 1, 100, 29)

# // 方格只有一行，机器人能到达所有方格
def test4():
    test("Test4", 10, 1, 10, 10)

# // 方格只有一列，机器人只能到达部分方格
def test5():
    test("Test5", 15, 100, 1, 79)

# // 方格只有一列，机器人能到达所有方格
def test6():
    test("Test6", 15, 10, 1, 10)

# // 方格只有一行一列
def test7():
    test("Test7", 15, 1, 1, 1)

# // 方格只有一行一列
def test8():
    test("Test8", 0, 1, 1, 1)

# // 机器人不能进入任意一个方格
def test9():
    test("Test9", -10, 10, 10, 0)


test1()
test2()
test3()
test4()
test5()
test6()
test7()
test8()
test9()
