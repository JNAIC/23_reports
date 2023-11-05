a = int(input())
list1 = input().split()
list2 = []
list3 = []
for i in list1:
    j = i[::-1]
    list2.append(j)
i = 0
while i < len(list1):
    list3.append(list1[i] == list2[i])
    i += 1
print(any(list3))
