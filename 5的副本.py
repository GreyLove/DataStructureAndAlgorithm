# 5、随机打乱数组
import random
def randomlyArray(list):
    if not list or len(list) < 2:
        return list
    j = 0
    l = len(list)-1
    for i in range(l):
        k = random.randint(i,l)
        tmp = list[k]
        list[k] = list[j]
        list[j] = tmp
        j += 1
    
    return list


print(randomlyArray([1,2,3,4,5]))