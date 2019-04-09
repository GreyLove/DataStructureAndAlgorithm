# #// 面试题59（一）：滑动窗口的最大值
# #// 题目：给定一个数组和滑动窗口的大小，请找出所有滑动窗口里的最大值。例如，
# #// 如果输入数组2, 3, 4, 2, 6, 2, 5, 1及滑动窗口的大小3，那么一共存在6个
# #// 滑动窗口，它们的最大值分别为4, 4, 6, 6, 6, 5，


def maxInWindows(num,size):
    if not num or len(num) == 0 or size<1:
        return []
    
    queue = []
    l = []
    for i in range(len(num)):

        if len(queue) and (i - queue[0]) >= size:
            queue.pop(0)

        while len(queue):
            if num[i] >= num[queue[-1]]:
                queue.pop()
            else:
                break

        queue.append(i)
        if i>=size-1:
            l.append(num[queue[0]])

    return l


num = [2, 3, 4, 2, 6, 2, 5, 1]
size = 3
#    4, 4, 6, 6, 6, 5

# num = [1, 3, -1, -3, 5, 3, 6, 7 ]
# size = 3
#    3, 3, 5, 5, 6, 7 

# num = [ 1, 3, 5, 7, 9, 11, 13, 15  ]
# size = 4
#    7, 9, 11, 13, 15

# num = [ 16, 14, 12, 10, 8, 6, 4 ]
# size = 5
#    16, 14, 12 

# num = [ 10, 14, 12, 11  ]
# size = 1
#    10, 14, 12, 11 

# num = [ 10, 14, 12, 11  ]
# size = 4
#    10, 14, 12, 11 

# num = [ 10, 14, 12, 11  ]
# size = 5
#    10, 14, 12, 11 

n = maxInWindows(num,size)
print(n)
