def get_longest_word(sentence):
    list1 = sentence.split()
    result = max(list1, key=len)
    return result

# 获取输入


sentence = input()

# 调用函数
print(get_longest_word(sentence))
