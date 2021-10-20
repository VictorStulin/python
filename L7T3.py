class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        res = self.number - other.number
        if res >= 0:
            return Cell(res)
        else:
            print('Невозможно выполнить операцию')

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, amount):
        order = ''
        for i in range(self.number // amount):
            order += '*' * amount + '\n'
        order += '*'* (self.number % amount)
        return order

    def __str__(self):
        return f'{self.number}'


my_cell_1 = Cell(12)
my_cell_2 = Cell(15)

print(my_cell_1 + my_cell_2)
print(my_cell_1 - my_cell_2)
print(my_cell_2 - my_cell_1)
print(my_cell_1 * my_cell_2)
print(my_cell_1 / my_cell_2)

print(my_cell_1.make_order(5))
print(my_cell_2.make_order(5))
