
def sqrt(x,p):
    if x < 0:
        return
    l = 0
    r = x
    m = (l+r)/2
    while abs(m**2-x) > p:
        if m**2 > x:
            r = m
        elif m**2 < x:
            l = m
        else:
            return m
        m = (l+r)/2

    return m

mid = sqrt(16,0.00001)
print(mid)