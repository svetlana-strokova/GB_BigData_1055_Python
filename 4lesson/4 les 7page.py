# 7 Задание. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
#При вызове функции должен создаваться объект-генератор.
#Функция должна вызываться следующим образом:
#for el in fibo_gen().

from itertools import count
from math import factorial

def fibo_gen():
    for el in count(1):
        yield factorial(el)

gen = fibo_gen()
x = 0
for i in gen:
    if x < 15:
        print(i)
        x += 1
    else:
        break