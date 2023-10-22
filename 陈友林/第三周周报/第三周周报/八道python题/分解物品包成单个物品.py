def break_down_list(items):
    list1 = []
    for i in items:
        quantity = i['quantity']         # 数量
        i['quantity'] = 1                # 把原来的字典转变为要添加入列表的字典
        while quantity != 0:             # 添加数量次字典进入列表
            list1.append(i)
            quantity -= 1
    return list1


# 获取物品列表
items = eval(input())
# 调用函数，输出分解后的物品列表
print(break_down_list(items))
# items = eval(input())
# for i in items:
#     quantity = i['quantity']
#     print(quantity)
