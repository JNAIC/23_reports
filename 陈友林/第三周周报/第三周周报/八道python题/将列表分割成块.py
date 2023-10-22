def list_into_chunks(num_list, chunk_size):
    i = len(num_list)
    j = chunk_size
    c = []
    k = i % j
    if k != 0:                       # 有剩余元素
        tail = num_list[i - k: i]    # 先把尾部多出来的取出来
        c.append(tail)
        i -= k
        while i != 0:                # 再把前面部分取出
            b = num_list[i - j: i]
            c.append(b)
            i -= j
    else:                            # 无剩余元素
        while i != 0:                # 再把前面部分取出
            b = num_list[i - j: i]
            c.append(b)
            i -= j
    c = c[::-1]           # 因为每次都在尾部添加所以要反转列表
    return c


num_list = list(map(int, input().split()))    # 从用户输入中获取块大小
chunk_size = int(input())                     # 调用函数
print(list_into_chunks(num_list, chunk_size))
