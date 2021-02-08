# 4 Задание Строка с пробелами, выводим каждое слово с новой строки, берем первые 10 букв в длинном слове

text = input('Введите произвольные слова через символ пробел - ')
text.split( )
text = text.split( )
#for element in text:
#    print(element)
i = 0
while i < len(text) :
    print( str(i + 1) + '. ' + str(text[i]) )
    i += 1

#2вариант
text = input("введите строку ")
my_word = []
num = 1
for el in range(text.count(' ') + 1):
    my_word = text.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word [el]}")
        num += 1
    else:
        print(f" {num} {my_word [el] [0:10]}")
        num += 1

