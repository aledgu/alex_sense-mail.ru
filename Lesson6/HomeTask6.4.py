
class Car:
    def __init__(self, speed, color, name, is_police=bool):
        self.car_speed = speed
        self.car_color = color
        self.car_name = name
        self.car_is_police = is_police
    def go(self):
        print(self.car_name, 'поехала')
    def stop(self):
        print(self.car_name, 'остановилась')
    def turn(self, direction):
        print(self.car_name , 'повернула на', direction)

class TownCar(Car):
    def show_speed(self):
        if self.car_speed > 60: print('Вы превышаете установленную скорость.')

class WorkCar(Car):
    def show_speed(self):
        if self.car_is_police == True: print('Пофиг на скорость мы беспредельщики XD')
        elif self.car_speed > 40: print('Вы превышаете устаовленную скорость')

my_car = Car(65, 'red', 'bestiya', False)
my_car.turn('levo')
town_car = TownCar(70, 'baklajan', 'lada_sedan', False)
town_car.turn('pravo')
town_car.show_speed()
work_car = WorkCar(100, 'banana', 'my_bah_x5', True)
work_car.show_speed()
print(my_car.car_is_police)