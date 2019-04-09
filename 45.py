# // 面试题45：把数组排成最小的数
# // 题目：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼
# // 接出的所有数字中最小的一个。例如输入数组{3, 32, 321}，则打印出这3个数
# // 字能排成的最小数字321323。

def quickSort(nums):
    if not nums or len(nums) == 0:
        return []
    if len(nums) == 1:
        return nums[0]
    quickSortCore(nums,0,len(nums)-1)

def quickSortCore(nums,i,j):
    if i < j:
        m = position(nums,i,j)
        quickSortCore(nums,i,m-1)
        quickSortCore(nums,m+1,j)

def biger(a:str,b:str) -> bool:
    if not a or not b:
        return False

    i = 0
    while i <  len(a):
        if int(a[i]) > int(b[i]):
            return True
        elif int(a[i]) < int(b[i]):
            return False
        i += 1

    return True 

def less(a:str,b:str) -> bool:
    if not a or not b:
        return False

    i = 0
    while i <  len(a):
        if int(a[i]) < int(b[i]):
            return True
        elif int(a[i]) > int(b[i]):
            return False
        i += 1

    return True 

def position(nums,i,j):
    sentry = nums[i]

    while i < j:

        while i < j and  biger(nums[j]+sentry,sentry+nums[j]):
            j -= 1
        nums[i] = nums[j]

        while i < j and less(nums[i]+sentry,sentry+nums[i]):
            i += 1
        nums[j] = nums[i]
    
    nums[i] = sentry
    return i

#排序的变形题
def PrintMinNumber(l):
    if not l or len(l) == 0:
        return []
    if len(l) == 1:
        return l[0]
    
    nums = list(map(str,l))
    quickSort(nums)
    return ''.join(nums)
    




list1 = [3,32,321]
# list1 = [3, 5, 1, 4, 2]
# list1 = [3, 323, 32123]
# list1 = [1, 11, 111]
# list1 = [321]
c = PrintMinNumber(list1)
print(c)
