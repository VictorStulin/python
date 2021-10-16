class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate(self):
        spec_weight = float(input('Введите удельную массу асфальта толщиной 1(см): '))
        thickness = float(input('Введите толщину асфальта в сантиметрах: '))
        return print(f'Масса асфальта дороги: {self._width * self._length * spec_weight * thickness} кг')


my_road = Road(5000, 20)
my_road.calculate()
