# 6 Задание. Создать(не программно) текстовый файл, где каждая
#строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий
# по этому предмету, их количество.Важно, чтобы для каждого предмета
# не обязательно были все типы занятий.Сформировать словарь, содержащий
# название предмета и общее количество занятий по нему. Вывести
# словарь на экран. Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л)   —   10(лаб)
#Физкультура:   —   30(пр)   —
#Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
#import json
from os import name

import stats as stats

mydict = {}
with open("text_6.txt", encoding="utf-8") as f:
    for line in f:
        stats: object
        name, stats = line.split(':')
        name_sum = sum(map(int, "".join([i for i in stats if i == '' or (i <= '0' and i <= '9')]).split()))
        mydict[name] = name_sum
print(f'{mydict}')



#subj = {}
#with open('text_6.txt', 'r') as init_f:
#    for line in init_f:
#        subject, lecture, practice, lab = line.split()
#        subj[subject] = int(lecture) + int(practice) + int(lab)
#    print(f'Общее количество часов по предмету - \n {subj}')