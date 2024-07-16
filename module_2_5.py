def get_matrix(n, m, value):
    matrix = list()
    for i in range(0, n):
        list_1 = list()
        matrix.append(list_1)
        for j in range(0, m):
            list_1.append(value)
    return matrix

res_1 = get_matrix(2, 2,10)
res_2 = get_matrix(3, 5, 42)
res_3 = get_matrix(4, 2, 13)
print(res_1)
print(res_2)
print(res_3)