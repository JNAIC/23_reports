# 关于字符串的函数

print（）打印函数

title（）以首字母大写的方式显示每个单词

upper（）字符串全部大写

lower（）字符串全部小写

f字符串

```python
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
```

\t 打印空格

\n 换行

rstrip（）删除字符串结尾多余空格（暂时）想要永久删除，必须将删除操作的结果关联到变量

```python
favorite_language = 'puthon '
favorite_language = favorite_language.rstrip()
favorite_language
```

```python
'python'
```

lstrip（）删除字符串开头多余空格（暂时）想要永久删除，必须将删除操作的结果关联到变量

strip（）删除字符串开头和结尾多余空格（暂时）想要永久删除，必须将删除操作的结果关联到变量

# 列表

```python
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[0])
#访问列表元素
```

*特殊语法：将索引指定为-1，返回最后一个列表元素。指定为-2，返回倒数第二个列表元素。（以此类推）

使用列表的值

```python
bicycles = ['trek','cannondale','redline','specialized']
message = f"My first bucycle was a {bicycles[0],title()}."
print(message)
```

```python
My first bucycle was a Trek.
```

append（）在列表末尾添加新元素

insert（'索引'，'元素'）在列表任意位置添加新元素

del语句删除元素

```python
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
del bicycles[0]
print(bicycles)
```

```python
['trek','cannondale','redline','specialized']
['cannondale','redline','specialized']
```

pop（）删除列表末尾元素（只是弹出列表，可以赋值给新的变量）

```python
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
popped_bicycles = bicycles.pop()
print(bicycles)
print(popped_bicycles)
```

```python
['trek','cannondale','redline','specialized']
['trek','cannondale','redline']
specialized
```

*pop  (0)  在圆括号中指定要删除元素的索引，来删除列表中任意位置元素

remove（）知道删除的值的删除方式

*只删除第一个指定的值，如果要删除的值在列表中出现多次，需要用循环来确保每个值都删除

sort（）永久性修改列表元素的排列顺序（字母顺序）

*sort（reverse=Trun）（字母倒序）

sorted（）对列表临时排序

```python
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
print(sorted(bicycles))
print(bicycles)
```

```python
['trek','cannondale','redline','specialized']
['cannondale','redline','specialized','trek']
['trek','cannondale','redline','specialized']
```

**sorted（reverse=Trun）（字母倒序）

len（）快速获悉列表长度

## 循环

循环打印名字

```python
cycles=['honda','yamaha','suzuki']
for cycle in cycles:
    print(cycle)
```

```python
honda
yamaha
suzuki
```

range（）打印一系列数

```python
for value in range(1,6):
    print(value)
```

```python
1
2
3
4
5
```

list（）将range（）的结果直接转化成列表

```python
num = list(range(1,6))
print(num)
```

```python
[1, 2, 3, 4, 5]
```

*range（）函数还可以指定步长，为此可以提供第三个参数

```python
num = list(range(2,11,2))
print(num)
```

```python
[2, 4, 6, 8, 10]
```

#创建一个列表，包含前十个数的平方

```python
num = []
for value in range(1,11):
    num.append(value**2)
print(num)
```

```python
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## 统计计算函数

min（）寻找数字列表最小值

max（）寻找数字列表最大值

sum（）数字列表求和

*列表解析

```python
squares = [value**2 for value in range(1,11)]
print(squares)
```

```python
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## 使用列表的一部分

切片

与range（）一样，在到达第二个索引之前的元素后停止（如果没有指定第一个索引，将自动从列表头开始。如果没有第二个索引，将自动从指定位置到结束。若想输出最后三名队员，可以  players [-3: ]  ）

```python
players = ['charles','martina','michael','florence','eli']
print(players[0:3])
```

```python
['charles', 'martina', 'michael']
```

遍历切片

```python
players = ['charles','martina','michael','florence','eli']
print("Here are the first three players on my team:")
for player in players[ :3]:
    print(player.title())
```

```python
Here are the first three players on my team:
Charles
Martina
Michael
```

复制列表

创建一个包含整个列表的切片

```python
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[ : ]
print("My favorit foods are:")
print(my_foods)
print("\nMy friend's favorit foods are:")
print(friend_foods)
```

```python
My favorit foods are:
['pizza', 'falafel', 'carrot cake']

My friend's favorit foods are:
['pizza', 'falafel', 'carrot cake']
```

注意：复制是把副本赋给新的列表

```python
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[ : ]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorit foods are:")
print(my_foods)
print("\nMy friend's favorit foods are:")
print(friend_foods)
```

```python
My favorit foods are:
['pizza', 'falafel', 'carrot cake', 'cannoli']

My friend's favorit foods are:
['pizza', 'falafel', 'carrot cake', 'ice cream']
```

## 元组

python将不能修改的值称为**不可变的**，而不可变的列表被称为**元组**。

定义元组：使用圆括号来标识，定义后，可以使用索引来访问其元素，和访问列表一样

```python
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
```

```python
200
50
```

*遍历同理与列表

修改元组变量

```python
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)
dimensions = (400,100)
for dimension in dimensions:
    print(dimension)
```

```python
200
50
400
100
```

# if语句

条件测试：检查是否相等（ == ）

检查是否相等是忽略大小写（使用lower（）函数）

检查是否不相等（ ！= ）

检查多个条件（and：都满足为True）（or：其中一个满足就为Ture）

检查特定值是否包含在列表中

```python
requested_toppings = ['mushrooms','onions','pineapple']
'mushrooms' in requested_toppings 
'pepperoni' in requested_toppings
```

```python
True
False
```

检查特定值是否不包含在列表中

```python
banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()},you can post a response if you wish.")
```

```python
Marie,you can post a response if you wish.
```

## 布尔表达式

条件测试的别名，其结果要么为True，要么为False。布尔值通常用于记录条件。

## if-else语句

```python
age = 17
if age >=18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are too young to vote.")
```

```python
Sorry, you are too young to vote.
```

## if-elif-else结构

```python
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
```

```python
Your admission cost is $25.
```

## 查找特殊元素

```python
requested_toppings = ['mushrooms','green peppers','extra chhes']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}")

print("\nFinished making your pizza!")    
```

```python
Adding mushrooms
Sorry, we are out of green peppers right now.
Adding extra chhes

Finished making your pizza!
```

## 确定列表不是空的

```python
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
```

```python
Are you sure you want a plain pizza?
```

# 字典

一个简单的字典

```python
alien_0 = {'color': 'green','points': 5}

print(alien_0['color'])
print(alien_0['points'])
```

```python
green
5
```

在python中，字典用放在花括号（ { } ）中的一系列键值对表示

**键值对**是两个相关联的值。指定键是，python将返回与之相关联的值。建和值之间用冒号分隔，二键值对之间用逗号分隔。在字典中，想存储多少个键值对都可以。

要获取与键相关联的值，可依次指定字典名和放在方括号内的键，如上面代码块所示，它将返回与其相关联的值。

## 添加键值对

字典是一种动态结构，可随时在其中添加键值对。要添加键值对，可依次指定字典名，用方括号括起来的键和相关联的值。

```python
alien_0 = {'color': 'green','points': 5}
print(alien_0)


alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

```

```python
{'color': 'green', 'points': 5}
{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
```

## 修改字典中的值

```python
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien now is {alien_0['color']}.")
```

```python
The alien is green.
The alien now is yellow.
```

## 删除键值对

```python
alien_0 = {'color': 'green','points': 5}
print(alien_0)

del alien_0['color']
print(alien_0)
```

```python
{'color': 'green', 'points': 5}
{'points': 5}
```

## 由类似对象组成的字典

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Srah's favorite language is {language}.")
```

```python
Srah's favorite language is C.
```

## 使用get（）来访问值

就字典而言，可使用方法get（）在指定的键不存在时返回一个默认值，从而避免这样的错误。

```python
alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
```

```python
No point value assigned.
```

如果字典中有键‘ points ‘ ，将获得与之相关的值；如果没有。将获得指定的默认值。

## 遍历字典

### 遍历所有键值

items() 函数以列表返回可遍历的(键, 值) 元组。将字典中的键值对以元组存储，并将众多元组存在列表中。

```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
```

```python
Key: username
Value: efermi

Key: first
Value: enrico

Key: last
Value: fermi
```

### 遍历字典中所有键

在不需要使用字典中的值时，方法keys（）很有用。

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())
```

```python
Jen
Sarah
Edward
Phil
```

### 按特定顺序遍历字典中的所有键

要以特定顺序返回元素，一种办法实在for循环中对返回的键进行排序。为此，可使用函数sorted（）来获得按特定顺序排序的键列表的副本：

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(name.title())
```

```python
Edward
Jen
Phil
Sarah
```

### 遍历字典中的所有值

如果主要对字典包含的值感兴趣，可以使用values（）来返回一个值列表，不包含任何键。

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for language in sorted(favorite_languages.values()):
    print(language.title())
```

```python
C
Python
Python
Ruby
```

这种做法提取字典中的所有值，而没有考虑是否重复。为剔除重复项，可以使用集合（set），**集合**中每个元素都必须是独一无二的：

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for language in set(favorite_languages.values()):
    print(language.title())
```

```python
Ruby
C
Python
```

通过对包含重复元素的列表调用set（），可让python找出列表中独一无二的元素，并使用这些元素来创建一个集合·。

*可使用一对花括号直接创建集合，并在其中用逗号分隔元素：

```python
languages = {'python','ruby','python','c'}
```

集合和字典很容易混淆，因为它们都是用一堆花括号定义的。当花括号内没有键值对时，定义很可能是集合。不同于列表和字典，集合不会以特定顺序存储元素。

## 嵌套

### 字典列表

```python
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green','point': 5,'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[ :5]:
    print(alien)
print("...")

print(f"Total number of aliens: {len(aliens)}")
```

```python
{'color': 'green', 'point': 5, 'speed': 'slow'}
{'color': 'green', 'point': 5, 'speed': 'slow'}
{'color': 'green', 'point': 5, 'speed': 'slow'}
{'color': 'green', 'point': 5, 'speed': 'slow'}
{'color': 'green', 'point': 5, 'speed': 'slow'}
...
Total number of aliens: 30
```

range（）返回一系列数，其唯一的用途是告诉python要重复这个循环多少次。

### 在字典中存储列表

```python
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra chees'],
}

print(f"You vordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
```

```python
You vordered a thick-crust pizza with the following toppings:
	mushrooms
	extra chees
```

### 在字典中存储字典

```python
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princetion',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}


for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
```

```python
Username: aeinstein
	Full name: Albert Einstein
	Location: Princetion

Username: mcurie
	Full name: Marie Curie
	Location: Paris
```