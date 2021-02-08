# 6 Задание про бгуна и дни до цели
while True:
    day = 1
    result_now = float(input('Начальный результат -'))
    result_target = float(input('Финальный результат -'))
    if result_now <= 0 or result_target < 0:
        print('Результат должен быть больше 0. Стартовое занчение != 0')
    else:
        while result_now < result_target:
            result_now *= 1.1
            day += 1
        print(f'Спортcмен добьется результат за {day} дней')
        break