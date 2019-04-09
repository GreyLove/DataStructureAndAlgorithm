# def sumToTarget(n,target):
#     if n < 0 or target < 0:
#         return 0

#     dic = {}
#     for k in range(target+1):
#         dic[k] = []
#     dic[0] = [[]]
#     for i in range(1,n+1):
        
#         nums = []
#         for key,val in dic.items():
#             if key <= target:

#                 for v in val:
#                     nums.append((key+i,v[:]+[i]))
        
#         for key,val in nums:
#             if key <= target:
#                 dic[key] += [val]

#     return dic[target]
        

# print(sumToTarget(5,7)) 


from collections import defaultdict


def sumToTarget(num,target):
    dic = defaultdict(list)
    dic[0] = [[]]
    for i in range(0,len(num)):
        cur = num[i]
        new_sums = []
        for key,val in dic.items():
            sum1 = key+cur
            if sum1 <= target:
                for v in val:
                    new_sums.append((sum1,v[:]+[cur]))
        for sum1, nums in new_sums:
            dic[sum1].append(nums)
        
    return dic[target]

print(sumToTarget([3,-7,2,4,1],7)) 