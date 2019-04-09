# // 面试题21：调整数组顺序使奇数位于偶数前面
# // 题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有
# // 奇数位于数组的前半部分，所有偶数位于数组的后半部分。


def ReorderOddEven_1(nums):
    if not nums:return
    
    i = 0
    j = len(nums)-1

    while i < j:
        
        while i < j and nums[i] & 1:
            i += 1
        
        while i < j and nums[j] & 1 == 0:
            j -= 1
        
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
        i += 1
        j -= 1





# numbers = [1, 2, 3, 4, 5, 6, 7]
# numbers = [1, 3, 5, 7, 2, 4, 6]
numbers = [2,3,3,5]
numbers = [1, 3, 5, 7, 2, 4, 6]
numbers = [2, 4, 6, 1, 3, 5, 7]
numbers = [1, 2, 3, 4, 5, 6, 7]

ReorderOddEven_1(numbers)
print(numbers)
