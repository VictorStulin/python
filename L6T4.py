class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return print(f'Машина {self.name} в движении')

    def stop(self):
        return print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        return print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        return print(f'Текущая скорость {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            output = print(f'Текущая скорость {self.speed}; скорость превышена')
        else:
            output = print(f'Текущая скорость {self.speed}')
        return output


class SportCar(Car):
    def warning(self):
        super().show_speed()
        if self.name == 'Ferrari':
            return print('На дороге спортивная машина')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            output = print(f'Текущая скорость {self.speed}; скорость превышена')
        else:
            output = print(f'Текущая скорость {self.speed}')
        return output


class PoliceCar(Car):
    def warning(self):
        if self.is_police is True:
            return print(f'На дороге полицейская машина {self.name}')


my_towncar = TownCar(80, 'black', 'Kia', False)
my_sportcar = SportCar(180, 'yellow', 'Lamborghini', False)
my_workcar = WorkCar(60, 'silver', 'Toyota', False)
my_policecar = PoliceCar(100, 'white', 'BMW', True)

print(my_towncar.speed)
print(my_sportcar.color)
print(my_workcar.name)
print(my_towncar.is_police)

my_towncar.show_speed()
my_policecar.warning()
my_sportcar.turn('влево')
my_workcar.stop()
