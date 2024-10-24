from threading import Thread
from time import sleep

class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        live = 100
        days = 0
        print(f'{self.name}, на нас напали!')

        while live > 0:
            live -= self.power
            sleep(1)
            days += 1
            if live < 0:
                print(f'{self.name}] сражается {days} день(дня)..., осталось 0 воинов.')
            else:
                print(f'{self.name}] сражается {days} день(дня)..., осталось {live} воинов.')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()