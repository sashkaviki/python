#Задача4:
'''Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).  А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен
показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.'''


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула' + ' ' + direction)

    def show_speed(self):
        print(f'Ваша скорость: {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости! Ваша скорость: {self.speed}')
        else:
            print(f'Ваша скорость: {self.speed}')


class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости! Ваша скорость: {self.speed}')
        else:
            print(f'Ваша скорость: {self.speed}')

class PoliceCar(Car):
    pass

towncar = TownCar(50, 'black', 'Honda', False)
workcar = WorkCar(100, 'red', 'Nissan', False)
towncar.show_speed()
towncar.stop()
towncar.go()
towncar.turn('на лево')
print(workcar.name)
workcar.stop()
workcar.show_speed()
sportcar = SportCar(130, 'red', 'Audi', False)
print(sportcar.name)
sportcar.show_speed()

