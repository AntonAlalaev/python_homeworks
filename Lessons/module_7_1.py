class Product:

    @staticmethod
    def create_list(raw_list):
        # Показалось, что удобнее сделать разбор
        # в классе продукта, т.к. в магазине могут быть и
        # другие сущности, которые также надо сохранять
        # на мой взгляд удобнее разбор хранить в самой сущности
        ref_list = []
        if len(raw_list) < 1:
            return ref_list
        for item in raw_list:
            split = str(item).replace(" ", "")
            split = str(split).replace("\n", "")
            split = str(split).split(",")
            if len(split) < 3:
                continue
            to_add = Product(split[0], float(split[1]), split[2])
            ref_list.append(to_add)
        return ref_list

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return str(f'{self.name}, {self.weight}, {self.category}')

    def __eq__(self, other):
        if isinstance(other, Product):
            if self.name == other.name and \
                    self.weight == other.weight and \
                    self.category == other.category:
                return True
        return False


class Shop:
    __file_name = "products.txt"

    def __load(self):
        # Загружает данные из файла
        with open(self.__file_name, 'r') as file_product:
            raw_data = file_product.readlines()
            file_product.close() # можно и не закрывать
        return Product.create_list(raw_data)

    def get_product(self):
        # Возвращает список из памяти.
        # Память у нас синхронизирована с файлом
        ret_string = ""
        for item in self.__product_list:
            ret_string += f"{item.__str__()}\n"
        return ret_string

    def __save_product(self):
        with open(self.__file_name, 'w') as file_product:
            for item in self.__product_list:
                file_product.writelines(str(item) + "\n")
            file_product.close() # можно и не закрывать

    def __init__(self):
        # Сначала попытаемся прочитать файл с продуктами,
        # чтобы наполнить базу
        self.__product_list = self.__load()

    def add(self, *other):
        for item in other:
            if not isinstance(item, Product):
                print("Добавляемый объект не является классом Product")
                continue
            else:
                if item in self.__product_list:
                    print(f"{item.name} уже есть в магазине")
                else:
                    self.__product_list.append(item)
        # После добавления перезаписываем список
        self.__save_product()


sh = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

sh.add(p1, p2, p3)

print(sh.get_product())
