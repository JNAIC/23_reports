# CreatTime :  2023/10/4 19:18
# 将数据输入到文件中
fp = open('D:/text.text','a+')
print('hellow,worled',file=fp)
fp.close()
# 不进行换行输出
print('hellow','worled','python')
