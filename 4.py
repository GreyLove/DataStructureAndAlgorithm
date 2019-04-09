# // 面试题4：二维数组中的查找
# // 题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按
# // 照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个
# // 整数，判断数组中是否含有该整数。


def find(matrix,num):
    if not matrix or len(matrix) == 0 or not isinstance(matrix[0],list) or len(matrix[0]) == 0:
        return False
    row = len(matrix)
    col = len(matrix[0])

    i = 0
    j = col-1

    while i<row and j>=0:
        v = matrix[i][j]
        if v == num:
            return True
        elif v > num:
            j -= 1
        else:
            i += 1
    
    return False

def Test(matrix,num,excepted):
    f = find(matrix,num)
    if f == excepted:
        print('**********success********',num)
    else:
        print('**********failtrue********',num)

matrix = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]

Test(matrix,7,True)

Test(matrix,5,False)

Test(matrix,0,False)

Test(matrix,1,True)

Test(matrix,15,True)


matrix = [[1,2,8,9]]

Test(matrix,7,False)

Test(matrix,5,False)

Test(matrix,1,True)

matrix = [[1],[2],[8],[9]]

Test(matrix,7,False)

Test(matrix,2,True)

Test(matrix,0,False)
