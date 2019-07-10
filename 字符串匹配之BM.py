# 1.核心的思想是 坏字符 和 好后缀 原则
# 2.坏字符 si - xi:  坏字符在 模式串中出现最后一次的位置(xi下标，如果没找到下标是-1)，防止滑动过多。
# si 模式串 和 主串 第一个不匹配的字符的下标。匹配是从大下标到小下标匹配的
# 3.只有坏字符的规则还是不行的，因为 可能有这种情况：aaaaaa , baa  这么 si 是0  xi是2 这样移动的是-2 ，向前移动了，所以这时候需要好后缀规则
# 4. aaabc 和 dbc  {bc} 是 好后缀记做{u},如果在模式串中 还有 相同的 子串 {bc}记做{u*} 那么就滑动到 模式串中 {u*} 中的位置
# 如果 {u} 在模式串没有，说明模式串的滑动还包含{u} 就不能匹配上，但是 主串中的好后缀部分{v} 和 模式串中前缀{v} 有重合，那么就滑动到前缀的位置
# 5.如果选择好后缀规则还是坏字符规则，那么看哪个移动的更多


def matchOfBM(s, p):
    if not s or not p:
        return -1
    if len(s) < len(p):
        return -1
    # 每个字符出现的位置
    p_dic = {}
    for k in range(len(p)):
        p_dic[p[k]] = k

    m = len(p)
    n = len(s)
    suffix = [-1 for _ in range(m)]
    prefix = [False for _ in range(m)]
    for i in range(m-1):
        j = i
        k = 0
        while j >= 0 and p[j] == p[m-1-k]:
            j -= 1
            k += 1
            suffix[k] = j+1

        if j == -1:
            prefix[k] = True

    i = 0
    while i <= n-m:

        # 找到坏字符
        j = m-1
        while j >= 0:
            if s[i+j] != p[j]:
                break
            j -= 1
            
        if j == -1:
            return i

        # x 为坏字符下标

        x = j-(p_dic[s[i+j]] if s[i+j] in p_dic else -1)
        y = 0

        if j < m-1:  # 因为j< m-1 说明 坏字符不是模式串在最后一位，需要 好后缀规则
            # 看看好后缀在模式中有没有
            k = m-1-j  # 好后缀长度
            h = suffix[k]
            if h != -1:  # 在模式串中有好后缀
                y = j - suffix[k] + 1
            else:  # 匹配好后缀中的部分，模式的前缀匹配好后缀的部分
                r = j + 2  # +2 是因为 j 是坏字符，+1 是 好后缀，不会进当前的这个条件会走上一个，因为一定会匹配到，所以+2
                while r <= m-1:
                    if prefix[m-r]:  # 尽量多的去匹配
                        y = r
                    r += 1
            if y == 0:  # 说明没匹配到
                y = m

        masx = max(x, y)
        i += masx

    return -1


s = 'abcacabcbcbacabc'
p = 'cbacabc'


i = matchOfBM(s, p)
print(i)
