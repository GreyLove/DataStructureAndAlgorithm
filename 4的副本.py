#4、判断输入字符串是否是合法的IP地址

#ipv4
def isValidIP(list):
    if not list:
        return False
    if len(list) < 7 or len(list) > 15:
        return False
    i = 0
    j = 0
    pointNum = 0
    while j < len(list):
        if (ord(list[j]) >= ord('0') and  ord(list[j]) <= ord('9')) \
        or ord(list[j]) == ord('.'):
            if list[j] == '.':
                pointNum += 1
                if pointNum>3:
                    return False
                if j-i > 3 or j-i < 1:
                    return False
                tmpStr = list[i:j] 
                if tmpStr[0] == '0' and j-i>2:
                    return False
                tmp = int(tmpStr)
                if tmp>255 or tmp<0:
                    return False
                i = j+1
                if i > len(list)-1 or list[i] == '.':
                    return False
                j = i
            else:
                j = j+1
        else:
            return False
    return True


ipArr = ["abc", "123456789012345678", ".1.2.3", "1.2.3.4.", "1.2.3", "1.2.3.4.5", "1.02.003.014", "1a.2.3.4", "1.2a.3.4", "1.2.3a.4", "1.2.3.4a",
            "0.1.2.3", "-1.1.2.3", "1.-1.2.3", "1.2.-1.3", "1.2.3.-1", "256.1.2.3", "1.256.2.3", "1.2.256.3", "1.2.3.256", "1234.123.123.123", "123.1234.123.123",
            "123.123.1234.123", "123.123.123.1234", "123.123.123.123", "0.0.0.0", "1.0.0.0", "255.255.255.255", "11.22.33.44", "",'1.1.1.1.1','1..1.1.1','1.1.1.1..']

for k in ipArr:
    print(k,"----",isValidIP(k))

# print(isValidIP('1.1.1.1.1'))
# print("----",isValidIP("1.02.003.014"))

