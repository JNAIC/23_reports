from random import*
target = randint(1,99)
times = 7
print('猜数字游戏开始，请猜100以内的整数')
while times != 0:
    num = int(input('请输入你要猜的数字：\n'))
    if num > target:
        print('你输入的数字有点大，请继续猜！\n')
        times -= 1
        continue
    elif num < target:
        print('你输入的数字有点小，请继续猜！\n')
        times -= 1
        continue
    else:
        print('恭喜你，猜对了！')
