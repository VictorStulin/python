class MyException(Exception):
    def __init__(self, txt):
        self.obj = txt


a = 5
b = 0
try:
    if b == 0:
        raise MyException('На ноль деление не определено')
    a / b
except MyException as err:
    print(err)
