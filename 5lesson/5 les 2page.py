# 2 Задание. Создать текстовый файл (не программно), сохранить
#в нем несколько строк, выполнить подсчет количества строк,
#количества слов в каждой строке.

my_file = open('text_2.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('text_2.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
my_file = open('text_2.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1} - ой строки {len(content[i])}')
my_file = open('text_2.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()

#2 вариант
with open('text_2.txt', r,encoding='utf-8') as f:
    usefulness = (f'{line}. {" ".join(count.split())} - {len(count.split())} слов' for line, count in enumerate(f, 1))
    print(*usefulness, f'всего строк - {len(usefulness)}.', sep='\n')

lines_n = 0
words_n = 0
f = open('text_2.txt', 'r')
for line in f:
    lines_n += 1
    words = line.split()
    words_n += len(words)
f.close()
print(lines_n)
print(words_n)