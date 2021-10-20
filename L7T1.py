class Matrix:
    def __init__(self, array):
        self.array = array

    def __str__(self):
        line_new = ''
        for line in range(len(self.array)):
            for i in range(len(self.array[line])):
                line_new += f'{(self.array[line][i])}  '
            line_new += '\n'
        return line_new

    def __add__(self, other):
        new_array = self.array
        for line in range(len(self.array)):
            for i in range(len(self.array[line])):
                new_array[line][i] = self.array[line][i] + other.array[line][i]
        return Matrix(new_array)


my_matrix_1 = Matrix([[1, 2, 3], [1, 2, 3]])
my_matrix_2 = Matrix([[4, 5, 6], [4, 5, 6]])
my_matrix_3 = my_matrix_1 + my_matrix_2
print(my_matrix_3)
print(my_matrix_1)
