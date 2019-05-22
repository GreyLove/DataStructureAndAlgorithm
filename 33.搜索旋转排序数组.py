#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
class Solution:
    def search(self, nums, target: int) -> int:
        if not nums:
            return -1
        i = 0
        j = len(nums)-1
        a = nums
        mid = i
        # 找到最小值的分界点
        while a[i] >= a[j]:
            if j-i == 1:
                mid = j
                break
            mid = (i+j) >> 1
            if a[i] == a[mid] and a[j] == a[mid]:
                for k in range(i,j):
                    if a[k] < a[mid]:
                        mid = k
                break
           
            elif a[mid] >= a[i]:#i - mid 递增
                i = mid
            elif a[mid] <= a[j]:#mid - j 递增
                j = mid
        # 锁定分区
        i = 0
        j = len(nums)-1
        if mid == 0:
            pass
        elif mid == j:
            if target == nums[-1]:
                return j
            else:
                j = mid-1
        elif target >= a[mid] and target <= a[j]:
            i = mid
        elif target >= a[0] and target <= a[mid-1]:
            j = mid-1
        
        while i <= j:
            m = (i+j)>>1
            if a[m] == target:
                return m
            elif a[m] > target:
                j = m-1
            elif a[m] < target:
                i = m+1
        
        return -1



i = Solution().search([4,5,6,7,0,1,2],4)
print(i)
