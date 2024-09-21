first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x,y:x==y, first, second)))

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name,'a',encoding='UTF=8') as file:
            for i in range(len(data_set)):
                file.write(f'{str(data_set[i])}\n')
        return file_name
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'],('Питер', 'Москва','Челябинск'))

from random import choice
class MysticBall:
    def __init__(self,*words):
        self.words = words

    def __call__(self):
        random_item = choice(self.words)
        return random_item

first_ball = MysticBall('Да', 'Нет', 'Наверное','Может быть','Неужели')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())


