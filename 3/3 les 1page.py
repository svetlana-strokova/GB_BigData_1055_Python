# 1 Задание.Реализовать функцию, принимающую два числа
# (позиционные аргументы) и выполняющую их деление.
from unittest import result


def div(*args):
    try:
        arg1 = int(input("Введите делимое -  "))
        arg2 = int(input("Введите делитель -  "))
        res = arg1 / arg2
    except ValueError:
        return 'Ошибка значения'
    except ZeroDivisionError:
        return 'Ошибка. На ноль делить нельзя'

    return res

print(f'Результат деления -  {div()}')
