class Data:
    def __init__(self, data_input):
        self.data_input = data_input

    def __repr__(self):
        return f'{self.data_input}'

    @classmethod
    def type_transformer(cls, data_input):
        data_input = data_input.split('-')
        date = int(data_input[0])
        month = int(data_input[1])
        year = int(data_input[2])
        return date, month, year

    @staticmethod
    def data_validation(data_input):
        data_input = Data.type_transformer(data_input)
        if data_input[1] > 12:
            print(f'Неверно указан месяц {data_input[1]}')

        if data_input[0] > 31:
            print(f'В месяце должно быть меньше дней')
        elif data_input[0] > 30 and data_input[1] != (1 or 2 or 3 or 5 or 7 or 8 or 10 or 12):
            print(f'В этом месяце ({data_input[1]}) меньше дней')
        elif data_input[1] == 2 and data_input[0] == 30:
            print(f'В феврале меньше дней')
        elif data_input[1] == 2 and data_input[0] == 29:
            if data_input[2] % 400 == 0 or (data_input[2] % 4 == 0 and data_input[2] % 100 != 0):
                pass
            else:
                print(f'В феврале меньше дней в невисикосном году ')


data_entered = '29-02-2021'
my_data = Data(data_entered)
print(my_data.type_transformer(data_entered))
print(my_data.data_validation(data_entered))
