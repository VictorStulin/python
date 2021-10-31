class ComplexNumbers:
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return f'{self.number}'

    def real_im(self):
        im_part = []
        real = 0
        imag = 0
        number_array = self.number.split('+')
        for el in number_array:
            if 'i' in el:
                new_el = el.replace('i', '')
                im_part.append(new_el)
                number_array.remove(el)
        real_part = number_array
        for i in real_part:
            real += int(i)
        for i in im_part:
            imag += int(i)
        return real, imag

    def __add__(self, other):
        real = self.real_im()[0] + other.real_im()[0]
        imag = self.real_im()[1] + other.real_im()[1]
        return ComplexNumbers(f'{real}+{imag}i')

    def __mul__(self, other):
        real = self.real_im()[0] * other.real_im()[0] - self.real_im()[1] * other.real_im()[1]
        imag = self.real_im()[0] * other.real_im()[1] + self.real_im()[1] * other.real_im()[0]
        return ComplexNumbers(f'{real}+{imag}i')


my_number_1 = ComplexNumbers('5i')
my_number_2 = ComplexNumbers('6i+1+2+3+3i')
print(my_number_1.real_im())
print(my_number_2.real_im())
print(my_number_1 + my_number_2)
print(my_number_1 * my_number_2)
