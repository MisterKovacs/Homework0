data_structure = [[1, 2, 3],
                  {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}),
                  "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])
                  ]

list_all = list()
def calculate_structure_sum(*args):
    def recursion_func(item):
        if isinstance(item, (list, tuple, set)):
            for i in item:
                recursion_func(i)
        elif isinstance(item, dict):
            for key, value in item.items():
                recursion_func(key)
                recursion_func(value)
        else:
            list_all.append(item)
    recursion_func(data_structure)
    a = 0
    for j in list_all:
        if isinstance(j, (int, float)):
            a += j
        elif isinstance(j, str):
            a += len(j)
    return a


result = calculate_structure_sum(*data_structure)
print(result)