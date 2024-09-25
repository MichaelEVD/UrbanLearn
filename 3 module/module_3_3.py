def print_params(a = 1, b = 'строка', c = True) :
    print(a,b,c)


print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(1,'Vasya', False)
print_params('Petya', 48, (1,2,3))


values_list = [7,'Ira', False]
values_dict = {'a':'Anna','b':[12,34,56], 'c':(1,2,3)}


print_params(*values_list)
print_params(**values_dict)


values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)