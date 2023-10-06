str = 'Hello World'
a = -1
mp = dict()
for i in str:
    if i in mp:
        mp[i] += 1
    else:
        mp[i] = 1
for j in range(len(str)):
    if mp[str[j]] == 1:
        a = j
        break
print(a)
