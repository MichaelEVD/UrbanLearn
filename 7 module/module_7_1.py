from pprint import pprint
class Product:
    def __init__(self,name,weight,category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return '{}  {}  {} '.format(
            self.name, self.weight, self.category)

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name,'r')
        products = file.read()
        file.close()
        return products

    def add(self,*products):
        current_products = self.get_products()
        file1 = open(self.__file_name, 'a')
        for product in products:
            if str(product) not in current_products:
                file1.write(str(product)+"\n")
                current_products += str(product)+"\n"
            else:
                print(f'Продукт {product} уже есть в списке!')
        file1.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1,p2,p3)

print(s1.get_products())
