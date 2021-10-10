#не включая 240
my_list = [item for item in range(20, 240) if item % 20 == 0 or item % 21 == 0]
print(my_list)
