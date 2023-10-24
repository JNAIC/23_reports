def list_into_chunks(num_list, chunk_size):    
    # 此处编写代码 
    list_1=[]
    for i in range(0,len(num_list),chunk_size):
        list_1.append(num_list[i:i+chunk_size]) 
    return list_1 
# 从用户输入中获取数据，并将其转换为列表
num_list = list(map(int, input().split()))
# 从用户输入中获取块大小
chunk_size = int(input())
# 调用函数
print(list_into_chunks(num_list, chunk_size))