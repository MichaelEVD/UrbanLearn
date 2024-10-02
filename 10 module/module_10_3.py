import threading
import random
from time import sleep
class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            replenishment = random.randint(50,500)
            self.balance = self.balance + replenishment
            print(f'Пополнение: {replenishment}. Баланс: {self.balance}')
            sleep(0.001)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()


    def take(self):
        for i in range(100):
            reducing = random.randint(50,500)
            print(f'Запрос на {reducing}')
            if reducing <= self.balance :
                self.balance = self.balance - reducing
                print(f'Снятие: {reducing}. Баланс: {self.balance}')
            else:
                print(f'"Запрос отклонён, недостаточно средств" ')
                self.lock.acquire()


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
