from threading import Thread, Lock
from random import random, randint
from time import sleep

class Bank(Thread):
    def __init__(self):
        self.balance = 0
        self.lock = Lock()
        super().__init__()

    def deposit(self):
        for i in range(1, 100):
            ran_deposit = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += ran_deposit
            print(f"Пополнение: {ran_deposit}. Баланс: {self.balance}")
            sleep(0.001)

    def take(self):
        for i in range(1, 100):
            ran_withdraw = randint(50, 500)
            print(f"Запрос на снятие {ran_withdraw}")
            if self.balance < ran_withdraw:
                print("Запрос отклонен. Недостаточно средств")
                self.lock.acquire()
            else:
                self.balance -= ran_withdraw
                print(f"Снятие: {ran_withdraw}. Баланс: {self.balance}")
            sleep(0.001)
bank = Bank()

th1 = Thread(target=Bank.deposit, args=(bank,))
th2 = Thread(target=Bank.take, args=(bank,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bank.balance}')

