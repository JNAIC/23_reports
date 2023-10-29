# 用你的代码替换 ___

# 定义函数length_of_last_word，用于打印最后一个单词的长度
def length_of_last_word(sentence):

    # 将句子分割成单词
    words_list = sentence.split()

    # 获取最后一个单词的长度
    result = len(words_list[-1])

    # 如果句子的末尾有标点符号`.`，从结果中删除它
    if words_list[-1][-1] == ".":
        result -= 1

    print(result)


# 调用函数
length_of_last_word(input())
