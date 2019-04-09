# #// 面试题15：二进制中1的个数
# #// 题目：请实现一个函数，输入一个整数，输出该数二进制表示中1的个数。例如
# #// 把9表示成二进制是1001，有2位是1。因此如果输入9，该函数输出2。

def NumberOf1_Solution1(number):
    if number == 0:
        return 0
    
    k = 63

    count = 0
    while k >= 0:
        if (number)&(1<<k)>0:
            count += 1
        k -= 1
    
    return count
    


def NumberOf1_Solution2(number):
    if number == 0:
        return 0
    
    count = 0
    while number > 0:
        if number & 1 > 0:
            count += 1
        number = number >> 1
    
    return count


#// ====================测试代码====================
def Test(number, expected):

    actual = NumberOf1_Solution1(number)
    if (actual == expected):
        print("Solution1: Test for %d passed.\n"% number)
    else:
        print("Solution1: Test for %d failed.\n"% number)

    actual = NumberOf1_Solution2(number)
    if (actual == expected):
        print("Solution2: Test for %d passed.\n"% number)
    else:
        print("Solution2: Test for %d failed.\n"% number)

    print("\n")


#// 输入0，期待的输出是0
Test(0, 0)

#// 输入1，期待的输出是1
Test(1, 1)

#// 输入10，期待的输出是2
Test(10, 2)

#// 输入0x7FFFFFFF，期待的输出是31
Test(0x7FFFFFFF, 31)

#// 输入0xFFFFFFFF（负数），期待的输出是32
Test(0xFFFFFFFF, 32)

#// 输入0x80000000（负数），期待的输出是1
Test(0x80000000, 1)

