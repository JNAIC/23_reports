i = eval(input())
for t in range(2,i):
    if i % t == 0:
        print("{}不是素数".format(i))
        break
    else:
        print("{}是素数".format(i))
        break
