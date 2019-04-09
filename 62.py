# // 面试题62：圆圈中最后剩下的数字
# // 题目：0, 1, …, n-1这n个数字排成一个圆圈，从数字0开始每次从这个圆圈里
# // 删除第m个数字。求出这个圆圈里剩下的最后一个数字。


from MyList import *

def LastRemaining_Solution1(num,k):
    if num <= 0:
        return False

    head = CreateListNode(0)
    cur = head
    for i in range(1,num):
        node = CreateListNode(i)
        cur.m_pNext = node
        cur = node
    cur.m_pNext = head
    
    while head.m_pNext != head:
        cur = head
        for i in range(1,k):
            cur = cur.m_pNext

        # print(cur.m_nValue)
        nextNode = cur.m_pNext
        cur.m_nValue = nextNode.m_nValue
        cur.m_pNext = nextNode.m_pNext
        head = cur
    
    print(head.m_nValue)
    return head


    
# 高效的数学方法
def LastRemaining_Solution2(n, m):
    if n < 1 or m<1:
        return -1
    
    last = 0
    for i in range(2,n+1):
        last = (last+m)%i
    
    print(last)
    return last






n = 3
k = 3
LastRemaining_Solution1(n,k)
LastRemaining_Solution2(n,k)
