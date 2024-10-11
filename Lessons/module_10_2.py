from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, knight_name, power):
        self.knight_name = knight_name
        self.power = power
        self.enemies = 100
        super().__init__()

    def run(self):
        print(f"{self.knight_name} на нас напали!")
        day_counter = 0
        while self.enemies > 0:
            self.enemies -= self.power
            day_counter += 1
            sleep(1)
            print(f"{self.knight_name}, сражается {day_counter} день (дня) осталось {self.enemies} воинов.")
        print(f"{self.knight_name} одержал победу спустя {day_counter} дней (дня)")


first_knight = Knight("Sir Lancelot", 10)
first_knight.start()
second_knight = Knight("Sir Galahad", 20)
second_knight.start()

first_knight.join()
second_knight.join()
print("Все битвы закончились!")
