class Animal:
    """
    Базовый класс животного
    """

    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def __str__(self):
        return self.name

    def eat(self, food):
        if isinstance(food, Plant) and food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        elif isinstance(food, Plant):
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Plant:
    """
    Базовый класс растения
    """

    def __init__(self, name):
        self.name = name
        self.edible = False


class Mammal(Animal):
    """
    Наследуемый класс млекопитающего
    """

    def __init__(self, name):
        super().__init__(name)


class Predator(Animal):
    """
    Наследуемый класс хищника
    """

    def __init__(self, name):
        super().__init__(name)


class Flower(Plant):
    """
    Наследуемый класс цветка, по умолчанию несъедобный
    """

    def __init__(self, name):
        super().__init__(name)


class Fruit(Plant):
    """
    Наследуемый класс фрукта, по умолчанию съедобный
    """

    def __init__(self, name):
        super().__init__(name)
        self.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
