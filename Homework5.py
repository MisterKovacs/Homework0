immutable_var = 1, 2, True, "String"
print(immutable_var)
   # immutable_var[2] = False
   # print(immutable_var)
   # кортеж является неизменяемым объектом.
mutable_var = [1, 2, True, "String"]
mutable_var[2] = False
print(mutable_var)