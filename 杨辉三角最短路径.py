def minPath(nums):
    if not nums:
        return 0
    n = len(nums)
    f1 = nums[n-1]
    i = n-2
    while i >= 0:
        f2 = []
        for j in range(len(f1)-1):
            f2.append(min(f1[j],f1[j+1]))
        
        f1 = []
        for j in range(len(f2)):
            f1.append(nums[i][j]+f2[j])
        i -= 1
    return f1[0]

nums = \
[
[1],
[3,2],
[6,5,4],
[10,9,8,7],
[15,14,13,12,11]
]

print(minPath(nums))
