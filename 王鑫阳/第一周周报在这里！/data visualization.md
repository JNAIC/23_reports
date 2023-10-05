```python
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
```
#### Summary
- Trend
	- [lineplot](#lineplot)
- Relationship
	- [barplot](#barplot)
	- [heatmap](#heatmap)
	- [scatterplot](#scatterplot)
		- lmplot
		- regplot
		- swarmplot
- Distribution
	- [histplot](#histgram)
	- [kdeplot](#KDE)
		- jointplot

## 10.03
#### lineplot
- **load data**
	`data_name=pd.read_csv(file_name,index_col="Date",parse_dates=True)`
	这里的`parse_dates`指的是解析日期，将读入的`index_col`解析为时间日期，一般默认为False
- **plot**
	```python
	plt.figure(figsize=(14,6))
	#设置图形的长宽（这里的plt是导入的matplotlib.pyplot模块）
	plt.title("this is a title")
	#设置标题
	sns.lineplot(data=dataframe_name.column_1,label='column_1')
	sns.lineplot(data=dataframe_name.column_2,label='column_2')
	#sns表示使用seaborn，lineplot表示要绘制一个折线图
	plt.xlabel('Date')

	#创建一个包含两个数据集的折线图，底部标签为日期
	```
- `list(dataframe_name.columns)` 列出dataframe的各个列索引
- 绘制图形一般包含：
	1. 图像标题
	2. x轴及其名称
	3. y轴及其名称

## 10.04

#### barplot
```python
data_name=pd.read_csv(file_name,index_col="Month")
plt.figure(figsize=(10,6))
plt.title("this is a title")
sns.barplot(x=data_name.index,y=data_name.column_name)
#x轴为导入数据的行索引（会自动将行索引的标题,即Month，作为xlabel）
#y轴为导入数据的列索引
plt.ylabel=("this is a ylabel")
#设置ylabel
```
- ==设置数据的行索引时不能使用`x=date_name.Month`，因为Month以及被设为数据中行索引的标题==

#### heatmap
```python
plt.figure(figsize=(10,6))
plt.title("this is a title")
sns.heatmap(data=data_name,annot=True)
#annot=True（这一般默认为False）指明要在色块上显示数值
plt.xlabel("this is a xlabel")
```

#### scatterplot
```python
sns.scatterplot(x=data_name.column_name1,y=data_name.column_name2)

sns.regplot(x=data_name.column_name1,y=data_name.column_name2)
#也可以绘制散点图，但是会多增加一条线性回归的直线
#reg就是regression（回归）的意思

sns.scatterplot(x=data_name.column_name1,y=data_name.column_name2,hue=data_name.column_name3)
#同样绘制了一个散点图，但是以column_name3为颜色分类依据

sns.lmplot(x='column_name1',y='column_name2',hue='column_name3',data=data_name)
#与regplot相似，为hue分类出来的两个集合建立回归直线
#lm就是liner model（线性模型）的意思

#需要注意的是在lmplot中使用了一个新的书写方式
#即在最后加上data_name，这种书写方法也可以用于scatterplot中，即：
sns.scatterplot(x='column_name1',y='column_name2',hue='column_name3',data=data_name)
#但是不加上的方法却不能用于lmplot

sns.swarmplot(x='column_name1',y='column_name2',data=data_name)
#绘制一个蜂群图
```

#### histgram
```python
sns.histplot(data_name.column_name)
#创建一个直方图，统计每个区间内数据点的数量
sns.histplot(data=data_name,x='column_name',hue='column_Name')
#为数据集中的所有元素创建一个直方图，通过hue进行分类
```
#### KDE
```python
sns.kedplot(data_name.column_name,shade=True)
#创建一个KDE(kernel density esitimate 核密度)图
#其中shade=True的作用是填充曲线下方区域
sns.kedplot(data=data_name,x='cloumn_name',hue='column_Name',shade=True)
#创建一个包含多个数据集的KDE图，通过hue进行分类
sns.jointplot(x='column_name1',y='column_name2',data=data_name,kind='kde')
#创建一个2D的KDE图
```
