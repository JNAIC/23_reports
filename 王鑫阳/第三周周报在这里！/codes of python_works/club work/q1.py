def can_form_palindrome(word) :
    new_word = word
    cnt1 = 0 # 计数出现次数为单数的字符
    cnt2 = 0 # 单次的
    for i in set(word) :
        if word.count(i) % 2 == 0 :
            new_word = new_word.replace(i,'')
        if word.count(i) % 2 != 0 and word.count(i) != 1:
            cnt1 += 1
        if word.count(i) == 1 :
            cnt2 += 1
    if cnt1 > 1 or cnt2 > 1:
        return "False"
    else :
        return "True"

word = input()

print(can_form_palindrome(word))