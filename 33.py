# #// 面试题33：二叉搜索树的后序遍历序列
# #// 题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# #// 如果是则返回true，否则返回false。假设输入的数组的任意两个数字都互不相同。


def VerifySquenceOfBST(sequence,start,end):
    if sequence == None or len(sequence) == 0:
        return False
    
    if start < end:
        m = start
        r = False
        root = sequence[end]
        for i in range(start,end):
            if sequence[i] < root:
                if r:
                    return False
                m = i
            else:
                r = True
        VerifySquenceOfBST(sequence,start,m)
        VerifySquenceOfBST(sequence,m+1,end-1)
    
    return True



#// ====================测试代码====================
def Test(testName, sequence, length,  expected):

    if(testName != None):
        print("%s begins: " %  testName)
    end = len(sequence)-1 if sequence else 0
    expected1 = VerifySquenceOfBST(sequence, 0,end) if sequence else False
    if(expected1 == expected):
        print("passed.\n")
    else:
        print("failed.\n")


#//            10
#//         /      \
#//        6        14
#//       /\        /\
#//      4  8     12  16
def Test1():

    data = [4, 8, 6, 12, 16, 14, 10]
    Test("Test1", data, 0, True)


#//           5
#//          / \
#//         4   7
#//            /
#//           6
def Test2():

    data = [4, 6, 7, 5]
    Test("Test2", data, 0, True)


#//               5
#//              /
#//             4
#//            /
#//           3
#//          /
#//         2
#//        /
#//       1
def Test3():

    data = [1, 2, 3, 4, 5]
    Test("Test3", data, 0, True)


#// 1
#//  \
#//   2
#//    \
#//     3
#//      \
#//       4
#//        \
#//         5
def Test4():

    data = [5, 4, 3, 2, 1]
    Test("Test4", data, 0, True)


#// 树中只有1个结点
def Test5():

    data = [5]
    Test("Test5", data, 0, True)


def Test6():

    data = [7, 4, 6, 5]
    Test("Test6", data, 0, False)


def Test7():

    data = [4, 6, 12, 8, 16, 14, 10]
    Test("Test7", data, 0, False)


def Test8():

    Test("Test8", None, 0, False)


Test1()
Test2()
Test3()
Test4()
Test5()
Test6()
Test7()
Test8()
