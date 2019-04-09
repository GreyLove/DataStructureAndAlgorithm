# // 面试题10：斐波那契数列
# // 题目：写一个函数，输入n，求斐波那契（Fibonacci）数列的第n项。

def Fibonacci(n):
    if n < 0:
        return
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a = 0
    b = 1
    
    for _ in range(2,n+1):
        c = a+b
        a = b
        b = c
    
    return c


print(Fibonacci(0))
print(Fibonacci(1))
print(Fibonacci(2))
print(Fibonacci(3))
print(Fibonacci(4))
print(Fibonacci(5))
print(Fibonacci(6))
