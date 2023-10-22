def list_into_chunks(num_list, chunk_size):  
    new_list = []
    fin_list = []
    Num_list = num_list
    for i in range(len(num_list)) :
        new_list.append(Num_list[i])
        if (i+1)%chunk_size == 0 :
            fin_list.append(new_list)
            num_list = num_list[chunk_size:]
            new_list = []
    if len(num_list) != 0 :
        fin_list.append(num_list)
    return fin_list

num_list = list(map(int, input().split()))

chunk_size = int(input())

print(list_into_chunks(num_list, chunk_size))