def extreme_words_in_sentence(sentence):
    sen = sentence.split()
    length = []
    for i in sen :
        length.append(len(i))
    max_str = sen[length.index(max(length))].lower()
    min_str = sen[length.index(min(length))].lower()
    ans = (max_str,min_str)
    return ans

sentence = input()

print(extreme_words_in_sentence(sentence))