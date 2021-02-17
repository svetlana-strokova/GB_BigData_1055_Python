# 5 Задание. Создать (программно) текстовый файл, записать в него программно
#набор чисел, разделенных пробелами. Программа должна
#подсчитывать сумму чисел в файле и выводить ее на экран.

def summary():
    try:
        with open('numbers_5_page.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильный ввод. Ошибка ввода-вывода')
summary()

# 2 вариант
from random import randint
with open('numbers_5_page.txt', mode='w+', encoding='utf-8') as f:
    f.writes("".join([str(randint(1, 1000)) for _ in range(100000)]))
    f.seek(0)
    print(sum(map(int, f.readline().spli())))