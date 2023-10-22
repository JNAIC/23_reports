def break_down_list(items):
    breaked_items = []
    for i in items :
        for j in range(i['quantity']) :
            i['quantity'] = 1
            breaked_items.append(i)
    return breaked_items

items = eval(input())

print(break_down_list(items))