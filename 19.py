# // 面试题19：正则表达式匹配
# // 题目：请实现一个函数用来匹配包含'.'和'*'的正则表达式。模式中的字符'.'
# // 表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题
# // 中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"
# // 和"ab*ac*a"匹配，但与"aa.a"及"ab*a"均不匹配。


def match(string, pattern):
    if string == None or pattern == None:
        return False
    if len(string) == 0 and len(pattern) == 0:
        return True
    return matchCore(string, pattern,0,0)

def matchCore(string, pattern,i,j):

    if i == len(string) and j == len(pattern):
        return True
    
    if j >= len(pattern):
        return False
    
    if j+1<len(pattern) and pattern[j+1] == '*':
        if j < len(pattern) and i<len(string) and (string[i] == pattern[j] or pattern[j] == '.'):
            return matchCore(string, pattern,i+1,j) or \
                    matchCore(string, pattern,i+1,j+2) or \
                        matchCore(string, pattern,i,j+2)
        else:
            return matchCore(string, pattern,i,j+2)

    if j < len(pattern) and i<len(string) and (string[i] == pattern[j] or pattern[j] == '.'):
        return matchCore(string, pattern,i+1,j+1)
    
    return False



# // ====================测试代码====================
def Test(testName, string, pattern, expected):
    if(testName != None):
        print("%s begins: "% (testName))

    if(match(string, pattern) == expected):
        print("Passed.")
    else:
        print("FAILED.")

Test("Test01", "", "", True)
Test("Test02", "", ".*", True)
Test("Test03", "", ".", False)
Test("Test04", "", "c*", True)
Test("Test05", "a", ".*", True)
Test("Test06", "a", "a.", False)
Test("Test07", "a", "", False)
Test("Test08", "a", ".", True)
Test("Test09", "a", "ab*", True)
Test("Test10", "a", "ab*a", False)
Test("Test11", "aa", "aa", True)
Test("Test12", "aa", "a*", True)
Test("Test13", "aa", ".*", True)
Test("Test14", "aa", ".", False)
Test("Test15", "ab", ".*", True)
Test("Test16", "ab", ".*", True)
Test("Test17", "aaa", "aa*", True)
Test("Test18", "aaa", "aa.a", False)
Test("Test19", "aaa", "a.a", True)
Test("Test20", "aaa", ".a", False)
Test("Test21", "aaa", "a*a", True)
Test("Test22", "aaa", "ab*a", False)
Test("Test23", "aaa", "ab*ac*a", True)
Test("Test24", "aaa", "ab*a*c*a", True)
Test("Test25", "aaa", ".*", True)
Test("Test26", "aab", "c*a*b", True)
Test("Test27", "aaca", "ab*a*c*a", True)
Test("Test28", "aaba", "ab*a*c*a", False)
Test("Test29", "bbbba", ".*a*a", True)
Test("Test30", "bcbbabab", ".*a*a", False)
Test("Test31", "aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c", False)
