s = input()
cha = 0
spa = 0
num = 0
ano = 0
for i in s:
    if i.isalpha():
        cha += 1
    elif i.isdigit():
        num += 1
    elif i.isspace():    #判断空格
        spa += 1
    else:
        ano += 1
print(f'中英文字母有{cha}个，数字有{num}个，空格有{spa}个，其他字符有{ano}个。')
