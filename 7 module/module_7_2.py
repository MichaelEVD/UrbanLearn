def custom_write(file_name, strings):
    file = open(file_name,'a',encoding = 'utf-8')
    strings_positions = dict()
    for i in range(len(strings)):
        strings_positions.update({(i + 1,file.tell()): strings[i]})
        file.write(str(strings[i]) + '\n')
    return strings_positions
    file.close()

info = ['Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!']

result = custom_write('test.txt',info)
for elem in result.items():
  print(elem, sep='\n')
