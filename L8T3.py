class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


el = ''
el_array = []
while el != 'stop':
    el = input('Введите число (stop - команда остановки программы): ')
    try:
        if not el.isnumeric():
            raise MyException('Неверный тип данных, введите число')
        el_array.append(el)
        print(el_array)

    except MyException as err:
        print(err)
print(el_array)
