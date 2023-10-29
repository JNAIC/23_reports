# 请在 ___ 划线处，替换成你的代码

# 创建正方形类Square
class Square:
    # 实现 __init__() 函数，初始化属性
    def __init__(self, length):
        self.length = length

    # 实现面积方法 get_area() ，并返回面积
    def get_area(self):
        s = self.length ** 2
        return s

    # 实现周长方法 get_perimeter() ，并返回周长
    def get_perimeter(self):
        c = self.length * 4
        return c


# 输入一个整数
length = int(input())

# 创建Square类对象
squrare = Square(length)

# 调用 get_area() 方法并打印面积
print(squrare.get_area())

# 调用 get_perimeter() 方法并打印周长
print(squrare.get_perimeter())
