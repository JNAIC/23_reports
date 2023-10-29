import re
sen = input()
sen = re.findall(r'\w+', sen)
length = [len(i) for i in sen]
max_str = sen[length.index(max(length))]
min_str = sen[length.index(min(length))]
print(max_str)
print(min_str)