# 第三周python

# 这周一直在排练学院和百团等演出内容,学的内容比较少
# 以下是这周的python学习内容:

## 元组 (不可修改)

tu=(1,2,True,"hey","hey")

### 空元组 
t1=()
t2=tuple()

###元组操作

num=tu.index(1)
numm=tu.count("hey")
nummm=len(tu)
print(num,numm,nummm)

## 字符串可作为储存容器 (只读不可修改)
my_str="aLdsifast"
value=my_str[3]
print(value)

### 字符串操作
val=my_str.index("a")
nmy_str=my_str.replace("d","3")
####replace,split,strip得到的是新字符串 旧的不改变
print(nmy_str)

print(nmy_str.split("s"))
print(nmy_str.strip("at"))

index=0
while index<len(nmy_str):
    print(nmy_str[index])
    index+=1

## 序列

### 切片

my_list=[0,1,2,2,2,3,5]
print(my_list[3:6:2])
print(my_list[::-2])

## 集合(元素不重复,无序)
coll={1,2,3,4}

### 空集合
col=set()
set1=(2,3,5,5,6)
### 集合操作

#### pop取出后原集合就没了
col.add(2)
col.add(3)
col.remove(2)
col.pop()
col.clear()
col.difference(set1)
col.difference_update
col.union(set1)

## 字典
dic1={"a":99,"b":88,"c":77}
print(dic1["a"])

### 字典操作

#### 新增元素(若原有则覆盖)
dic1["d"]=66

#### pop取出并删除,clear清除,keys获取全部key
print(dic1.pop("a"))
k=dic1.keys()
for key in k:
    print(key)
    print(dic1[key])

## 数据容器通用函数
print(max(dic1))
print(min(dic1))

### 类型转换

list(dic1)
str(dic1)
tuple(dic1)
set(dic1)

### 容器排序(结果是列表形式)
sorted(dic1)
sorted(dic1,reverse=True)

## 函数多个返回值

def test_r():
    return 1,2,3
x,y,z=test_r()
print(y)

# 下周的话可能要准备百团啥的 时间不太多,但会抽时间学的!!争取早点学完python基础内容!一起加油qaq
