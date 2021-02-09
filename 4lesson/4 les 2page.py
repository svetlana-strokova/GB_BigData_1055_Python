# 2 Задание Вывести элементы списка, значения которых больше предыдущего элемента.
#Для формирования списка использовать генератор.

my_list = [25, 4, 6, 1, 7, 8, 2, 12]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')