# 4 Задание. Из целого положительного числа найти самую большую цифру, используя while и математические операции

question = int(input('Введите любое целое, положительное число -'))
maximum = question % 10
num = question
while num > 0:
    digit = num % 10 #Нахождение остатка от деления на 10 - извлекается последняя цифра числа
    # (а деление нацело на 10 - // 10 - удаляет последнюю цифру числа)
    if digit > maximum:
        maximum = digit
        if digit == 9:
            break

    num = num // 10
    print(num)

print(f"Наибольшая цифра в числе {question} равна {maximum}")
