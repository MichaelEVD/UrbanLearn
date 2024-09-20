first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
full_list = list(zip(first,second))
first_result =(len(x[0]) - len(x[1]) for x in full_list if len(x[0]) != len(x[1]))
second_result = (True if len(first[i]) == len(second[i]) else False for i in range(0,len(first)))


print(list(first_result))
print(list(second_result))