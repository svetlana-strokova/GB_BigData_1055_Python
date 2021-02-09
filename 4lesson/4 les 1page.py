# 1 Задание.Реализовать скрипт c функцией расчета заработной платы сотрудника

#from sys import argv

#script_name, time, salary, bonus = argv
#try:

#    time = int(time)
#    salary = int(salary)
#    bonus = int(bonus)
#    res = time * salary + bonus
#    print(f'Заработная плата сотрудника  {res}')
#except ValueError:
#    print('Введите число')

# 2 вариант
def sal():
    try:
        time = float(input('Выработка в часах - '))
        salary = int(input('Ставка -  '))
        bonus = int(input('Премия - '))
        res = time * salary + bonus
        print(f'Заработная плата сотрудника  {res}')
    except ValueError:
        return print('Введите число')
sal()

