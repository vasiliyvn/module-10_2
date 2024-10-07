from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self,name:str,power:int):
        super().__init__()
        self.name = name
        self.power = power
    def run(self):
        total = 100
        day = 0
        print(f'{self.name}, на нас напали!')
        while total!=0:
            day += 1

            total = total - self.power
            print(f'{self.name} сражается {day}день(дня)..., осталось {total} воинов.')
            sleep(1)
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()


print(f'Все битвы закончились!')