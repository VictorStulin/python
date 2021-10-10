from sys import argv
from itertools import count, cycle

print(argv)
# первый аргумент - начальная позиция первого скрипта; второй аргумент - условие остановки второго скрипта

# script1
for i in count(int(argv[1])):
    if i > 20:
        break
    else:
        print(i)

# script2
my_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
stop = 0

for month in cycle(my_list):
    if stop < int(argv[2]):
        print(month)
        stop += 1
    else:
        break
