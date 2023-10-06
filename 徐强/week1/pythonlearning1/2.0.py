# CreatTime :  2023/10/4 21:04
#转义字符#  \ +转义功能的首字母
print('hello\nworld')#  n-->newline的首字母表示换行
print('hello\tworld')
print('helloo00\tworld')#对比4 5 \t只有在字符胀满了四个空格后才会重新开四个空格
print('hello\rworld')#\r表示将光标退回至本行开头输入，所以后面的词把前面的就会全面覆盖
print('hello\raaa')
print('hello\bworld')#\b是退了一个，把o退没了
print('http:\\\\www.bing.com')
print("老师说：’大家好‘")
print('老师说：\'大家好\'')

# 原字符，不希望字符串中的转义字符起作用，使用原字符，就是在字符串之前加上r或R
print(R'hello\nworld')
# 注意事项，最后一个字符不能是反斜杠
print(R'hello\nworld\')
print(R'hello\nworld\\')