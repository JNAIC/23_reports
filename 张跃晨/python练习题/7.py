def break_down_list(items):
    # 此处编写代码 
    list0=[]
    for dic in items:#dic可以为{“type:"HB","quantity":2}
        value=dic["type"]#HB
        n=dic["quantity"]#2
        dic_new={"type":value,"quantity":1}
        for i in range(n):
            list0.append(dic_new)
    return list0

    
    
# 获取物品列表 
items = eval(input())
# 调用函数，输出分解后的物品列表
print(break_down_list(items))