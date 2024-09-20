first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
full_list = list(zip(first,second))
d = []
first_result =(len(x[0]) - len(x[1]) for x in full_list if len(x[0]) != len(x[1]))
for elem in first_result:
    d.append(elem)
print(d)
d =[]
second_result = (True if len(first[i]) == len(second[i]) else False for i in range(0,len(first)))
for elem in second_result:
    d.append(elem)
print(d)