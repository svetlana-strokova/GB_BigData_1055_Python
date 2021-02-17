# 4 Задание.Реализуйте базовый класс Car. У данного класса должны быть
# следующие атрибуты: speed, color, name, is_police (булево).А также методы:
# go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
# свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} начинает движение'

    def stop(self):
        return f'{self.name} останавливается'

    def turn_right(self):
        return f'{self.name} поворот направо'

    def turn_left(self):
        return f'{self.name} поворот налево'

    def show_speed(self):
        return f'Текушая скорость {self.name} - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name} - {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} выше текущей скорости городского автомобиля - '
        else:
            return f'Скорость {self.name} нормальная для городского автомобиля'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текушая скорость рабочего автомобиля {self.name} - {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} выше текущей скорости рабочего автомобиля'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из полицейского департамента'
        else:
            return f'{self.name} не из полицейского департамента'


jaguar = SportCar(100, 'Red', 'Jaguar', False)
kia = TownCar(30, 'White', 'KIA', False)
skoda = WorkCar(70, 'Rose', 'Skoda', True)
ford = PoliceCar(110, 'Blue',  'Ford', True)
print(skoda.turn_left())
print(f'Когда {kia.turn_right()}, тогда {jaguar.stop()}')
print(f'{skoda.go()} когда скорость точно {skoda.show_speed()}')
print(f'{skoda.name} цветом: {skoda.color}')
print(f'{jaguar.name} полицейский автомобиль? {jaguar.is_police}')
print(f'{skoda.name}  полицейский автомобиль? {skoda.is_police}')
print(jaguar.show_speed())
print(kia.show_speed())
print(ford.police())
print(ford.show_speed())
