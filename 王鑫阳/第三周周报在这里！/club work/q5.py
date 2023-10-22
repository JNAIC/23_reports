def get_unique_elements(nested_tuples):
    unique_num_list = list(set([a for b in nested_tuples for a in b]))
    unique_num_list.sort()
    return unique_num_list

nested_tuples = []

for _ in range(3):
    tuple_elements = tuple(map(int, input().split()))
    nested_tuples.append(tuple_elements)

print(get_unique_elements(nested_tuples))