s = input()
if s[0] == 'M':
    print("星期一")
elif s[0] == 'W':
    print("星期三")
elif s[0] == 'T':
    if s[1] == 'u':
        print("星期二")
    else:
        print("星期四")
else:
    if s[1] == 'a':
        print("星期六")
    else:
        print("星期日")
