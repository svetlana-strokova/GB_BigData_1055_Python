# 1 Задание.Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка

my_f = open('new text.txt', 'w') #открыть файл на запись, если файла нет, то создается новый
line = input('Введите текст \n')
while line:
    my_f.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

my_f.close()
my_f = open('new text.txt', 'r') #чтение
content = my_f.readlines()
print(content)
my_f.close()

#2 вариант
with open('new text', w, encoding='utf-8') as f:
    while True:
        line = input('Ввдите новую строку - ')
        if not line:
            break
        f.write(f.{line}\n')
        print(line,file=f)




