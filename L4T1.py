from sys import argv
print(argv)
salary = int(argv[1]) * int(argv[2]) + int(argv[3])
print(f"Зарплпта с учётом премии: {salary}")
