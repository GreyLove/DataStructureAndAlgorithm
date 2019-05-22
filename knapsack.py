# 01背包问题，
# 看了看分析其实有些不明白的地方
# 难点，如何将状态方程转化成 代码
def DynamicKnapSack(value,weight,maxWeight):
    if maxWeight == 0:
        return 0
    if len(value) != len(weight):
        return 0

    c = [[0 for _ in range(maxWeight+1)] for _ in range(len(value)+1)]

    i = 0
    w = 1
    # 开始拿物品
    while i < len(value):
        # 在一定重量下，拿价值最大的物品
        # 因为从第一个开始拿
        w = 1
        while w <= maxWeight:
            if weight[i] <= w:#取max 因为 value[i],不保证每个数都是正数
                c[i][w] = max(c[i-1][w-weight[i]]+value[i],c[i-1][w])
            else:
                c[i][w] = c[i-1][w]
            w += 1
        i += 1
    
    return c[i-1][w-1]


v = [6,-9,12]
w = [1,2,3]
weight = 2
print(DynamicKnapSack(v,w,weight))

                 
                 
