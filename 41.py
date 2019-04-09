# // 面试题41：数据流中的中位数
# // 题目：如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么
# // 中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，
# // 那么中位数就是所有数值排序之后中间两个数的平均值。

from MyMaxHeap import *
from MyMinHeap import *

def GetMedian(nums):
    if not nums or len(nums) == 0:return
    if len(nums) == 1:return nums[0]
    
    maxHeap = MaxHeap()
    minHeap = MinHeap()

    flag = 0
    i = 0
    while i < len(nums):
        v = nums[i]
        if flag == 0:
            v1 = v
            if minHeap.size() and v > minHeap.top():
               v1 = minHeap.pop()
               minHeap.push(v)
            maxHeap.push(v1)
        else:
            v1 = v
            if maxHeap.size() and v < maxHeap.top():
                v1 = maxHeap.pop()
                maxHeap.push(v)
            minHeap.push(v1)

        flag = 1-flag
        i += 1

    return (minHeap.top()+maxHeap.top())/2
    

nums = [1,3,5,7,9,2,4,6,8,10]
# nums = [1,2,3,4,5,6,7,8,9,10]
# nums = [1,2,2,3,3,4]
# nums = [1,2]

m = GetMedian(nums)
print(m)
