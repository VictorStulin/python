class WarehouseOrg:
    def __init__(self, array_org):
        self.array_org = array_org

    def __repr__(self):
        return f'{self.array_org}'


    def give_org(self, model, div_name):
        if model in self.array_org:
            self.array_org.remove(model)
            div_name.take_org(model)
        else:
            print(f'Модели {model} нет на складе')

    def stock_org(self, model, div_name):
        if div_name.return_org(model):
            self.array_org.append(model)
        else:
            print(f'У подразделения {div_name} нет модели {model}')

    def type_org_review(self):
        for i in self.array_org:
            print(i)


class Org:
    def __init__(self, id, model):
        self.id = id
        self.model = model

    def __repr__(self):
        return f'{self.model}'


class Printer(Org):
    def __init__(self, id, model, printer_type):
        super(Printer, self).__init__(id, model)
        self.printer_type = printer_type
        self.org_type = 'Printer'


class Scanner(Org):
    def __init__(self, id, model, max_format):
        super(Scanner, self).__init__(id, model)
        self.max_format = max_format
        self.org_type = 'Scanner'


class Copier(Org):
    def __init__(self, id, model, copy_speed):
        super(Copier, self).__init__(id, model)
        self.copy_speed = copy_speed
        self.org_type = 'Copier'


class Division:
    def __init__(self, div_name, array_org):
        if not array_org:
            array_org = []
        self.div_name = div_name
        self.array_org = array_org

    def take_org(self, model):
        self.array_org.append(model)

    def return_org(self, model):
        if model in self.array_org:
            self.array_org.remove(model)
            return True
        else:
            return False

printer_1 = Printer(1, 'HP Jet', 'laser')
printer_2 = Printer(2, 'Cannon Blue', 'flow')
copier_1 = Copier(3, 'Xerox', 100)
copier_2 = Copier(4, 'LG Copy', 50)
scanner_1 = Scanner(5, 'Kyocera', 'A4')
scanner_2 = Scanner(6, 'Hitachi', 'A2')

my_warehouse = WarehouseOrg([printer_1, copier_1, scanner_1])
my_division = Division('Creators', [printer_2, copier_2, scanner_2])

print(my_warehouse.array_org)
print(my_division.array_org)
print(my_warehouse.type_org_review())

my_warehouse.give_org('HP Jet', my_division)
print(my_division.array_org)




