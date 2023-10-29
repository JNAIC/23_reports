def jdg(stu_info):
    n = 0
    if stu_info[1] > 80 and stu_info[5] >= 1:
        n += 8000
    if stu_info[1] > 85 and stu_info[2] > 80:
        n += 4000
    if stu_info[1] > 90:
        n += 2000
    if stu_info[1] > 85 and stu_info[4] == 'Y':
        n += 1000
    if stu_info[2] > 80 and stu_info[3] == 'Y':
        n += 850
    return n

T = int(input())
sumx = 0
name = []
scholar = []
for _ in range(T):
    stu_info = []
    stu = input().split()
    for i in stu:
        try:
            x = int(i)
            stu_info.append(x)
        except:
            stu_info.append(i)
    stu_m = jdg(stu_info)
    sumx += stu_m
    scholar.append(stu_m)
    name.append(stu_info[0])

max_stu_scholar = max(scholar)
max_index = scholar.index(max_stu_scholar)
win_name = name[max_index]

print(win_name)
print(max_stu_scholar)
print(sumx)