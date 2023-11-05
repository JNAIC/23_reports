pandas

**索引选择分配**

![image-20231101231609302](C:\Users\20241\AppData\Roaming\Typora\typora-user-images\image-20231101231609302.png)

访问某一列的第一个

![image-20231101231637996](C:\Users\20241\AppData\Roaming\Typora\typora-user-images\image-20231101231637996.png)

访问第一行

![image-20231101231655782](C:\Users\20241\AppData\Roaming\Typora\typora-user-images\image-20231101231655782.png)

一列

![image-20231102105554066](C:\Users\20241\AppData\Roaming\Typora\typora-user-images\image-20231102105554066.png)

第一列前三个

![image-20231102110823231](C:\Users\20241\AppData\Roaming\Typora\typora-user-images\image-20231102110823231.png)

抽取访问

![image-20231102111749991](C:\Users\20241\AppData\Roaming\Typora\typora-user-images\image-20231102111749991.png)

倒着访问

![image-20231102111810651](C:\Users\20241\AppData\Roaming\Typora\typora-user-images\image-20231102111810651.png)

![image-20231102162858734](C:\Users\20241\AppData\Roaming\Typora\typora-user-images\image-20231102162858734.png)

loc区别iloc

loc可以直接访问信息（字典，数组）：【0,10】包括0-10

iloc必须访问索引（列表）：【0-10】包括0-9

[pandas索引函数loc和iloc的区别_hanyunkaka的博客-CSDN博客](https://blog.csdn.net/hanyunkaka/article/details/120470899)

##set_index()##产生新的行————操作索引

*列出有相同索引的行产生列表*

![image-20231102163320743](C:\Users\20241\AppData\Roaming\Typora\typora-user-images\image-20231102163320743.png)

![image-20231102182039480](C:\Users\20241\AppData\Roaming\Typora\typora-user-images\image-20231102182039480.png)

附加条件： 和

![image-20231102181945505](C:\Users\20241\AppData\Roaming\Typora\typora-user-images\image-20231102181945505.png)

附加条件： 或

![image-20231102182012180](C:\Users\20241\AppData\Roaming\Typora\typora-user-images\image-20231102182012180.png)

分配修改

![image-20231102183535989](C:\Users\20241\AppData\Roaming\Typora\typora-user-images\image-20231102183535989.png)

*head（）只读前五行*