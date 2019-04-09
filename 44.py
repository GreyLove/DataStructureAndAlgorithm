##// 面试题44：数字序列中某一位的数字
##// 题目：数字以0123456789101112131415…的格式序列化到一个字符序列中。在这
##// 个序列中，第5位（从0开始计数）是5，第13位是1，第19位是4，等等。请写一
##// 个函数求任意位对应的数字。

def digitAtIndex(inputIndex):
    if inputIndex<0:
        return -1
    if inputIndex<10:
        return inputIndex
    
    k = 1
    base = 9
    s = 9
    while s<inputIndex:
        k += 1
        base *= 10
        s += k*base
    
    # k 位数
    #开始的数
    start = 10**(k-1)
    
    p = 1
    base = 9
    s = 10
    for _ in range(1,k-1):
        p += 1
        base *= 10
        s += p*base
    
    diff = inputIndex-s
    chu = int(diff/k)
    yu = diff%k

    start += chu
    l = []
    while start>0:
        l.append(start%10)
        start = int(start/10)
    
    return l[k-1-yu]






##// ====================测试代码====================
def test(testName, inputIndex, expectedOutput):

	if(digitAtIndex(inputIndex) == expectedOutput):
		print(testName," passed")
	else:
		print(testName," FAILED")



# test("Test1", 0, 0)
# test("Test2", 1, 1)
# test("Test3", 9, 9)
test("Test4", 10, 1)
test("Test5", 189, 9) #// 数字99的最后一位，9
test("Test6", 190, 1) #// 数字100的第一位，1
test("Test7", 1000, 3)#// 数字370的第一位，3
test("Test8", 1001, 7)#// 数字370的第二位，7
test("Test9", 1002, 0)#// 数字370的第三位，0
