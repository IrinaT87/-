# фунция генерации рандомного числа с записью его в лог с указанием даты и времени, с паузой в 1секунду

from datetime import datetime # модуль текущей даты и времени
from random import randint
import time #модуль с функцией sleep

def log(date):
    with open('log.txt', 'a') as file:
        data_time=datetime.now()
        file.write(f'{data_time}-{data} \n')

for i in range(100):
    data=randint(1,100)
    log(str(data))
    time.sleep(1)