# 5 Задание
revenue = float(input('Выручка, руб -'))  # при вводе int - "обрезается конец" цифры, если есть сотые
loss = float(input('Издержки, руб -'))
profit = revenue - loss  # Прибыль
if revenue > loss:
    print(f'Фирма получает прибыль {profit}')
    print(f'Рентабельность выручки - {profit / revenue:.3f}')
    people: int = int(input('Количество сотрудников -'))
    peop_prof = profit / people
    print(f'Прибыль на одного сотрудника, руб - {peop_prof:.3f} руб')
elif revenue < loss:
    print(f'Фирма терпит убытки {-profit}')
else:
    print(f"Стабильность - признак мастерства")
