# // 面试题49：丑数
# // 题目：我们把只包含因子2、3和5的数称作丑数（Ugly Number）。求按从小到
# // 大的顺序的第1500个丑数。例如6、8都是丑数，但14不是，因为它包含因子7。
# // 习惯上我们把1当做第一个丑数。

def GetUglyNumber_Solution1(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    
    root = 1
    time2 = []
    time3 = []
    time5 = []

    i2 = 0
    i3 = 0
    i5 = 0

    for _ in range(2,n+1):
        time2.append(root*2)
        time3.append(root*3)
        time5.append(root*5)

        root = time2[i2]
        if root > time3[i3]:
            root = time3[i3]

        if root > time5[i5]:
            root = time5[i5]
        
        if root == time2[i2]:
            i2 += 1
        if root == time3[i3]:
            i3 += 1
        if root == time5[i5]:
            i5 += 1
    
    return root
        
        


    
# // ====================测试代码====================
def Test(index, expected):

    if(GetUglyNumber_Solution1(index) == expected):
        print("solution1 passed\n")
    else:
        print("solution1 failed\n")



Test(1, 1)
Test(2, 2)
Test(3, 3)
Test(4, 4)
Test(5, 5)
Test(6, 6)
Test(7, 8)
Test(8, 9)
Test(9, 10)
Test(10, 12)
Test(11, 15)
Test(1500, 859963392)
Test(0, 0)

