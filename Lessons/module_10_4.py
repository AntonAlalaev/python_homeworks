from queue import Queue
from threading import Thread
from random import randint
from time import sleep


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, guest_name):
        self.guest_name = guest_name
        super().__init__()

    def run(self):
        wait_time = randint(3, 10)
        print(f"{self.guest_name} пришел и ждет")
        sleep(wait_time)
        print(f"{self.guest_name} ушел")


class Cafe:
    def __init__(self, *args):
        self.tables = list(args)
        self.queue = Queue()

    def is_there_any_guest(self):
        for table in self.tables:
            if table.guest is not None:
                return True
        return False

    def is_there_any_free_table(self):
        for table in self.tables:
            if table.guest is None:
                return True
        return False

    def arrange_guest(self, guest):
        guest_arranged = False
        for table in self.tables:
            if table.guest is None:
                table.guest = guest
                print(f"{guest.guest_name} сел за стол {table.number}")
                guest_arranged = True
                guest.start()
                break
        return guest_arranged

    def guest_arrival(self, *guests):
        for guest in guests:
            # Проверим заполнены ли столы
            if not self.arrange_guest(guest):
                self.queue.put(guest)
                print(f"{guest.guest_name} встал в очередь")

    def discuss_guests(self):
        while not self.queue.empty() or self.is_there_any_guest():
            for table in self.tables:
                if table.guest is not None:
                    if not table.guest.is_alive():
                        print(f"{table.guest.guest_name} поел и ушел.")
                        table.guest = None
                        print(f"Стол {table.number} свободен")
            if self.queue.empty() and not self.is_there_any_guest():
                continue
            if not self.queue.empty() and self.is_there_any_free_table():
                for table in self.tables:
                    if table.guest is None:
                        guest = self.queue.get()
                        table.guest = guest
                        print(f"{guest.name} вышел из очереди и сел за стол {table.number}")
                        guest.start()
                        break


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
