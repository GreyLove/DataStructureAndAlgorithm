# // 面试题16：数值的整数次方
# // 题目：实现函数double Power(double base, int exponent)，求base的exponent
# // 次方。不得使用库函数，同时不需要考虑大数问题。


def power(base,c):
    if c == 0:
        return 1
    k = c
    if c < 0:
        k = -c
    r = powerCore(base,k)

    if c < 0:
        r = 1/r
    
    return r
    
    
def powerCore(base,c):
    if c == 1:
        return base
    
    k = c >> 1
    result = power(base,k)
    result *= result
    if c & 1:
        result *= base
    
    return result


print(power(2,3))
print(power(0,3))
print(power(1,3))
print(power(-4,3))
print(power(2,-3))
