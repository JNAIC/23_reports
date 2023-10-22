def can(word):

    i = 0
    j = 0
    if len(word) % 2 == 0:       # 如果word长度为偶数
        while i < len(word):
            if word.count(word[i]) % 2 == 0:
                i += 1
            else:
                break
    else:                        # 如果word长度为奇数
        while i < len(word):
            if word.count(word[i]) % 2 == 0:
                i += 1
            else:
                j += 1
                i += 1
                if j > 1:
                    break
    if i == len(word):
        return True
    else:
        return False


word = input()
print(can(word))