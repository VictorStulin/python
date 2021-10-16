class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return print(f'Имя: {self.name}; Фамиля: {self.surname}')

    def get_total_income(self):
        return print(f"Совокупный доход: {int(self._income.get('wage')) + int(self._income.get('bonus'))}")


pos_1 = Position('Иван', 'Иванов', 'токарь', 30000, 40000)
pos_2 = Position('Пётр', 'Петров', 'слесарь', 35000, 35000)
pos_3 = Position('Elon', 'Musk', 'entrepreneur', 1, 10000000)
pos_1.get_full_name()
pos_1.get_total_income()
print(pos_2.position)
print(pos_2._income)
pos_3.get_full_name()
pos_3.get_total_income()
