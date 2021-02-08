# 5 Задание Реализовать структуру "Рейтинг"
numbers = [8, 5, 4, 4, 3, 2, 2]
print(f'Рейтинг - {numbers}')
digit = int(input('Введите число (111 - выход) '))
while digit != 111:
    for el in range(len(numbers)):
        if numbers[el] == digit:
            numbers.insert(el + 1, digit)
            break
        elif numbers[0] < digit:
            numbers.insert(0, digit)
        elif numbers[-1] > digit:
            numbers.append(digit)
        elif numbers[el] > digit and numbers[el + 1] < digit:
            numbers.insert(el + 1, digit)
    print(f'текущий список - {numbers}')
    digit = int(input("Введите число "))









