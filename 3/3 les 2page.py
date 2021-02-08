# 2 Задание Реализовать функцию, принимающую несколько параметров
# переменные
name = input('Введите имя - ')
surname = input('Введите фамилию - ')
year = int(input('Введите год рождения - '))
city = input('Введите город проживания - ')
email = input('Введите email - ')
telephone = input('Введите телефон - ')
#функция с возвращением кортежа
def my_func (name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])
print(my_func(name = 'Иван', surname = 'Иванов', year = '1988', city = 'Санкт-Петербург', email = 'email@mail.ru', telephone = '8-800-100-98-88'))






