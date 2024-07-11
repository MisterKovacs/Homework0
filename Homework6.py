    # Словари
my_dict = {'a':123, 'b':321, 'c':456}
print(my_dict)
print(my_dict['b'])
print(my_dict.get('x'))
my_dict.update({'d':654,
                'e':789})
del my_dict['c']
print(my_dict)
    # Множества
my_set = [1, 2, 3, 2, 1, 'String', 3, (1, 2, 3)]
my_set = set(my_set)
print(my_set.add(45.2))
print(my_set.add('Word'))
print(my_set)
print(my_set.discard('String'))
print(my_set)