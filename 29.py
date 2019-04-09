# // 面试题29：顺时针打印矩阵
# // 题目：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。


def PrintMatrixClockwisely(numbers):
    if numbers == None or len(numbers) == 0 or \
        not isinstance(numbers[0],list) or len(numbers[0]) == 0:
        return
    
    row = len(numbers)
    col = len(numbers[0])

    startX = 0

    while startX*2 < row and startX*2 < col:

        endX = row-startX-1
        endY = col-startX-1

        i = startX
        while i <= endY:
            print(numbers[startX][i])
            i += 1
        
        i = startX + 1
        while i <= endX:
            print(numbers[i][endY])
            i += 1
        
        i = endY-1
        while i >= startX and endX > startX:
            print(numbers[endX][i])
            i -= 1
        
        i = endX-1
        while i >= startX+1 and endY>startX:
            print(numbers[i][startX])
            i -= 1
        
        startX += 1
        









# // ====================测试代码====================
def Test( columns,  rows):
        print("Test Begin: %d columns, %d rows.\n" %  (columns, rows))

        if(columns < 1 or rows < 1):
                return

        numbers = []
        for i in range(rows):
                list = []
                for j in range(columns):
                        list.append( i * columns + j + 1)
                numbers.append(list)



        PrintMatrixClockwisely(numbers)

# /*
# 1    
# */
Test(1, 1)

# /*
# 1    2
# 3    4
# */
Test(2, 2)

# /*
# 1    2    3    4
# 5    6    7    8
# 9    10   11   12
# 13   14   15   16
# */
Test(4, 4)

# /*
# 1    2    3    4    5
# 6    7    8    9    10
# 11   12   13   14   15
# 16   17   18   19   20
# 21   22   23   24   25
# */
Test(5, 5)

# /*
# 1
# 2
# 3
# 4
# 5
# */
Test(1, 5)

# /*
# 1    2
# 3    4
# 5    6
# 7    8
# 9    10
# */
Test(2, 5)

# /*
# 1    2    3
# 4    5    6
# 7    8    9
# 10   11   12
# 13   14   15
# */
Test(3, 5)

# /*
# 1    2    3    4
# 5    6    7    8
# 9    10   11   12
# 13   14   15   16
# 17   18   19   20
# */
Test(4, 5)

# /*
# 1    2    3    4    5
# */
Test(5, 1)

# /*
# 1    2    3    4    5
# 6    7    8    9    10
# */
Test(5, 2)

# /*
# 1    2    3    4    5
# 6    7    8    9    10
# 11   12   13   14    15
# */
Test(5, 3)

# /*
# 1    2    3    4    5
# 6    7    8    9    10
# 11   12   13   14   15
# 16   17   18   19   20
# */
Test(5, 4)
