def apply_all_func(int_list, *functions):
    itog_list = {}
    for name in functions:
        result = name(int_list)
        itog_list.update({name.__name__:result})
    return itog_list


print(apply_all_func([6, 20, 15, 9],  max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))