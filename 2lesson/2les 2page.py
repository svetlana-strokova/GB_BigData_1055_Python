# 2 Задание обмен значений соседних элементов использовать функцию input
name0 = input('Введите произвольное мужское имя -')
name1 = input('Введите произвольное мужское имя -')
name2 = input('Введите произвольное женское имя -')
name3 = input('Введите произвольное женское имя -')
name4 = input('Введите произвольное мужское имя -')

text = [name0.title(), name1.title(), name2.title(), name3.title(), name4.title()]
print(text)
text[0] = name1
text[1] = name0
text[2] = name3
text[3] = name2
print(text)






