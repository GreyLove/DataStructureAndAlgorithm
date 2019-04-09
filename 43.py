# // 面试题43：从1到n整数中1出现的次数
# // 题目：输入一个整数n，求从1到n这n个整数的十进制表示中1出现的次数。例如
# // 输入12，从1到12这些整数中包含1 的数字有1，10，11和12，1一共出现了5次。

# 这题主要是思路问题，比较不好理解。在网上找了博客
# https://blog.csdn.net/yi_afly/article/details/52012593
# 主要是计算各个位1出现的个数，先算各位，然后十位。。。

# 时间复杂度O(log10N)
def NumberOf1Between1AndN_Solution1(n):
    if n<=0:
        return 0

    count = 0
    base = 1
    rounds = n

    while rounds > 0:
        weight = rounds%10
        rounds = int(rounds/10)
        count += rounds*base
        if weight>1:
            count += base
        elif weight == 1:
            count += n%base+1
        base *= 10
    
    return count
    
        

# // ====================测试代码====================
def Test(testName, n, expected):
    if(testName != None):
        print("%s begins: \n"% testName)
    
    if(NumberOf1Between1AndN_Solution1(n) == expected):
        print("Solution1 passed.\n")
    else:
        print("Solution1 failed.\n") 
    


    print("\n")

def Test1():

    # Test("Test1", 1, 1)
    # Test("Test2", 5, 1)
    Test("Test3", 10, 2)
    Test("Test4", 55, 16)
    Test("Test5", 99, 20)
    Test("Test6", 10000, 4001)
    Test("Test7", 21345, 18821)
    Test("Test8", 0, 0)

Test1()



