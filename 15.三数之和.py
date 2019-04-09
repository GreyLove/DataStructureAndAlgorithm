#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (20.43%)
# Total Accepted:    35.1K
# Total Submissions: 171.8K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？找出所有满足条件且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#
class Solution:
    def quickSort(self,nums):
        if not nums or len(nums)==0:
            return None
        self.quickSortCore(nums,0,len(nums)-1)
    
    def quickSortCore(self,nums,i,j):
        if i < j:
            m = self.position(nums,i,j)
            self.quickSortCore(nums,i,m-1)
            self.quickSortCore(nums,m+1,j)
        
    def position(self,nums,i,j):
        sentry = nums[i]
        while i < j:
            while i < j and nums[j] >= sentry:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] <= sentry:
                i += 1
            nums[j] = nums[i]

        nums[i] = sentry
        return i
    
    def contain(self,lists,item):

        for l in lists:
            i = 0
            j = 0
            while i < len(item) and j < len(l):
                if item[i] != l[j]:
                    break
                else:
                    i += 1
                    j += 1
            if i == 3 and j == 3:
                return True
        
        return False

                

    def threeSum(self, nums):
        if len(nums)<3:
            return []
        
        self.quickSort(nums)

        if nums[0]>0:
            return []
        
        if nums[-1]<0:
            return []
        
        lists = []
        k = 0
        while  k<len(nums) and nums[k]<=0:
            if k > 0 and nums[k] == nums[k-1]:
                k += 1
                continue
            i = k+1
            j = len(nums)-1

            while i < j:
                if i < j and nums[i]+nums[j]==-nums[k]:
                    l = [nums[k],nums[i],nums[j]]
                    lists.append(l)
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                elif i < j and nums[i]+nums[j]<-nums[k]:
                    i += 1
                elif i < j and nums[i]+nums[j]>-nums[k]:
                    j -= 1
            k += 1
        
        return lists
                


nums = [-1,0,1,2,-1,-4]
nums = [-2,0,0,2,2]
nums = [0,0,0,0]
nums = [-1,-2,-3,-4]
nums = [1,2,3,4]

n = Solution().threeSum(nums)
print(n)
        

