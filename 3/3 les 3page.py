# 3 Задание Три позиционных аргумента и вернуть сумму наибольших двух аргументов
#Функция
def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Result - {my_func(int(input("Введите первое число - ")), int(input("Введите второе число - ")), int(input("Введите третье число - ")))}')

