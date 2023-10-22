def extreme_words_in_sentence(sentence):
    sentence = sentence.lower()
    list1 = sentence.split()
    Max = max(list1, key=len)          # 定义长度为比较关键
    Min = min(list1, key=len)
    a = (Max, Min)
    return a


# 处获取输入
sentence = input()
# 调用函数
print(extreme_words_in_sentence(sentence))

