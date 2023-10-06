a = int(input('摄氏度请按1，华氏度请按2'))
if a == 1:
    b = float(input('请输入摄氏度：'))
    result = b*1.8 + 32
    print(f'你输入的是摄氏度{b},转换为华氏度是{result}。')
else:
    b = float(input('请输入华氏度：'))
    result = (b-32)/1.8
    print(f'你输入的是华氏度{b},转换为摄氏度是{result}。')
