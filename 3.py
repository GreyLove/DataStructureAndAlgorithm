#3、数组两个数的最大差

def miunsOfMax(list):
    if not list or len(list) < 2:
        return None
    min = list[0]
    max = list[0]
    for i in list:
        if i < min:
            min = i
        if i > max:
            max = i
    
    return max - min

print(miunsOfMax([1,2,3,4,5]))
print(miunsOfMax([2,4,3,1,5]))
