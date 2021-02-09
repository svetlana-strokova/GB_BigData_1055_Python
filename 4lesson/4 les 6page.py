# 6 Задание. Два скрипта: бесконечный интегратор-генератор и повторяющий элементы
#использовать функцию count() и cycle()модуля itertools.

from itertools import count

for el in count(int(input('Введите стартовое число - '))):
    print(el) # беконечный цикл!

from itertools import cycle

my_list = [True, 'ABC', 123, None]
for el in cycle(my_list):
    print(el) # беконечный цикл!


