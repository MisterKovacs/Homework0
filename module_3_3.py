def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)
print_params(2, 'word', False)
print_params()
print_params(1, 25, True)
print_params(1, 'string', [1, 2, 3])

print('-------------------------------------')

values_list = ['hi', True, 77]
values_dict = {'a':False, 'b':5, 'c':'bye'}
print_params(*values_list)
print_params(**values_dict)

print('-------------------------------------')

values_list_2 = ['everything', 4]
print_params(*values_list_2, 42)