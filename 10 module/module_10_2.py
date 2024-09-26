from threading import Thread
from time import sleep
class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        print(f"{self.name}, на нас напали!")
        count_days = int(100/self.power)
        war_days = 0
        for i in range(1, count_days+1):
            war_days += 1
            warriors = 100 - self.power*i
            print(f'{self.name} сражается {war_days} дней(день), осталось {warriors} воинов')
            sleep(1)
            if warriors <= 0:
                print(f"{self.name} одержал победу спустя {war_days} дней(дня)!")
            else:
                continue


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print(f'Все битвы закончились!')