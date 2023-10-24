def extreme_words_in_sentence(sentence):
    # 此处编写你的代码 
    list_0=sentence.split(" ")#将单词分开为列表中的元素
    #找出最长和最短的单词
    max_word=max(list_0,key=len)
    min_word=min(list_0,key=len)
    tuple0=(max_word.lower(),min_word.lower())
    return tuple0

# 处获取输入
sentence = input()
# 调用函数
print(extreme_words_in_sentence(sentence))