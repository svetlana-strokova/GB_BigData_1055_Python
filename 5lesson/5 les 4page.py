# 4 Задание. Создать (не программно) текстовый файл. Написать программу, открывающую файл на чтение
#и считывающую построчно данные. При этом английские
#числительные должны заменяться на русские.
#Новый блок строк должен записываться в новый текстовый файл.

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('numbers.txt', 'r') as file_obj:
    #content = file_obj.read().split('\n')
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('numbers_new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)

#2 вариант
from googletrans import Translator
with open('numbers_new.txt', encoding='utf-8') as nf:
    with open('numbers_new.txt', 'r', encoding='utf-8') as mf:
        text = mf.read()
    t = Translator()
    a = t.translate(text)
    print(a)

