# #// 面试题47：礼物的最大价值
# #// 题目：在一个m×n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值
# #// （价值大于0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或
# #// 者向下移动一格直到到达棋盘的右下角。给定一个棋盘及其上面的礼物，请计
# #// 算你最多能拿到多少价值的礼物？


def getMaxValue_solution1(values):
    if not values or len(values) == 0:
        return
    row = len(values)
    col = len(values[0])

    f = [[0 for _ in range(col)] for _ in range(row)]

    for i in range(row):
        for j in range(col):
            v = 0
            if i < row and j < col:
                if i > 0 and j>0:
                    v =  max(f[i-1][j],f[i][j-1])
                elif i > 0:
                    v = f[i-1][j]
                elif j > 0:
                    v = f[i][j-1]
            f[i][j] = v + values[i][j]
    
    return f[row-1][col-1]


#// ====================测试代码====================
def test(testName, values, rows, cols, expected):

    if(getMaxValue_solution1(values) == expected):
        print(testName,"solution1 passed.")
    else:
        print(testName,"solution1 FAILED.")

    # if(getMaxValue_solution2(values, rows, cols) == expected)
    #     std::cout << testName << ": solution2 passed." << std::endl
    # else
    #     std::cout << testName << ": solution2 FAILED." << std::endl


def test1():

    #// 三行三列
    values = [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]
    expected = 29
    test("test1",  values, 3, 3, expected)


def test2():

    #//四行四列
    values = [
        [ 1, 10, 3, 8 ],
        [ 12, 2, 9, 6 ],
        [ 5, 7, 4, 11 ],
        [ 3, 7, 16, 5 ]
    ]
    expected = 53
    test("test2",  values, 4, 4, expected)


def test3():

    #// 一行四列
    values = [
        [ 1, 10, 3, 8 ]
    ]
    expected = 22
    test("test3",  values, 1, 4, expected)


def test4():

    values = [
        [ 1 ],
        [ 12 ],
        [ 5 ],
        [ 3 ]
    ]
    expected = 21
    test("test4",  values, 4, 1, expected)


def test5():

    #// 一行一列
    values = [
        [ 3 ]
    ]
    expected = 3
    test("test5",  values, 1, 1, expected)


def test6():

    #// 空指针
    expected = 0
    test("test6", None, 0, 0, expected)


test1()
test2()
test3()
test4()
test5()
