from threading import Thread, Lock
import random

lock = Lock()
class Bank():
    def __init__(self, balance):
        super().__init__()
        self.balance = balance


    def deposit(self):
        for i in range(100):
            rep = random.randint(50, 501)
            if self.balance >= 500 and lock.locked():
                lock.release()
                self.balance += rep
            else:
                self.balance += rep

    def take(self):
        for j in range(100):
            relief = random.randint(50, 501)
            print(f'Запрос на {relief}')
            if relief <= self.balance:
                self.balance -= relief
                print(f'Снятие: {relief}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                lock.acquire()

bk = Bank(0)

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')