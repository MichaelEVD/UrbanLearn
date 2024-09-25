class House:
    def __init__(self, name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название:, {self.name}, кол-во этажей:,{self.number_of_floors}'

    # def __len__(self):
    #     return self.number_of_floors

    def __eq__(self, other):
        if not isinstance(other,int) and not isinstance(other,House):
            return f'Указанное число должно быть целым и относится к указанному классу'
        return self.number_of_floors == other.number_of_floors

    def __add__(self, value):
        if not isinstance(value,int) :
            return f'Указанное число должно быть целым'
        return self.number_of_floors + value


    def __gt__(self, other):
        if not isinstance(other,int) and not isinstance(other,House):
            return f'Указанное число должно быть целым и относится к указанному классу'
        return self.number_of_floors > other.number_of_floors


    def __ge__(self, other):
        if not isinstance(other,int) and not isinstance(other,House):
            return f'Указанное число должно быть целым и относится к указанному классу'
        return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):
        if not isinstance(other,int) and not isinstance(other,House):
            return f'Указанное число должно быть целым и относится к указанному классу'
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if not isinstance(other,int) and not isinstance(other,House):
            return f'Указанное число должно быть целым и относится к указанному классу'
        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        if not isinstance(other,int) and not isinstance(other,House):
            return f'Указанное число должно быть целым и относится к указанному классу'
        return self.number_of_floors != other.number_of_floors



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)

print(h1==h2)

h1.number_of_floors = h1.number_of_floors + 10
print(h1)
print(h1==h2)

h1.number_of_floors += 10
print(h1)

h2.number_of_floors = 10 + h2.number_of_floors
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)
