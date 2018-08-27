# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)
class TownCar:
    def __init__(self):
        self.speed = 90
        self.color = 'white'
        self.name = 'Town'
        self.is_police = False

    def go(self):
        print('Car is going')

    def stop(self):
        print('Car is stopping')

    def turn(self, direction):
        if direction == 'right':
            print('Car turn to the right')
        elif direction == 'left':
            print('Car turn to the left')


class SportCar:
    def __init__(self):
        self.speed = 300
        self.color = 'black'
        self.name = 'Sport'
        self.is_police = False

    def go(self):
        print('Car is going')

    def stop(self):
        print('Car is stopping')

    def turn(self, direction):
        if direction == 'right':
            print('Car turn to the right')
        elif direction == 'left':
            print('Car turn to the left')


class WorkCar:
    def __init__(self):
        self.speed = 70
        self.color = 'silver'
        self.name = 'Work'
        self.is_police = False

    def go(self):
        print('Car is going')

    def stop(self):
        print('Car is stopping')

    def turn(self, direction):
        if direction == 'right':
            print('Car turn to the right')
        elif direction == 'left':
            print('Car turn to the left')


class PoliceCar:
    def __init__(self):
        self.speed = 150
        self.color = 'blue'
        self.name = 'Police'
        self.is_police = True

    def go(self):
        print('Car is going')

    def stop(self):
        print('Car is stopping')

    def turn(self, direction):
        if direction == 'right':
            print('Car turn to the right')
        elif direction == 'left':
            print('Car turn to the left')


the_car = TownCar()
the_car.go()
the_car.stop()
the_car.turn('right')
the_car.turn('left')


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.
class Car:
    def __init__(self, car_type, car_model, car_color, car_speed, is_police=False):
        self.type = car_type
        self.model = car_model
        self.color = car_color
        self.speed = car_speed
        self.police = is_police

    def go(self):
        return 'Car is going'

    def stop(self):
        return 'Car is stopping'

    def turn(self, direction):
        return 'Car turn to the {}'.format(direction)


# Производный класс:
class Town_car(Car):
    def __init__(self, car_type, car_model, car_color, car_speed, is_police=False):
        super().__init__(car_type, car_model, car_color, car_speed, is_police=False)


class Sport_car(Car):
    def __init__(self, car_type, car_model, car_color, car_speed, is_police=False):
        super().__init__(car_type, car_model, car_color, car_speed, is_police=False)


class Work_car(Car):
    def __init__(self, car_type, car_model, car_color, car_speed, is_police=False):
        super().__init__(car_type, car_model, car_color, car_speed, is_police=False)


class Police_car(Car):
    def __init__(self, car_type, car_model, car_color, car_speed, is_police=False):
        super().__init__(car_type, car_model, car_color, car_speed, is_police=False)


police_car = Police_car('Police', 'car Rino', 'blue', '100 km/h', is_police=True)
print(police_car.type, police_car.model, police_car.color, police_car.go(), police_car.speed,
      police_car.turn('right'), police_car.stop())
