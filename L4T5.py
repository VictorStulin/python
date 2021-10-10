from functools import reduce


def item_mult(prev, cur):
    return prev * cur


my_list = [item for item in range(100, 1001) if item % 2 == 0]
print(my_list)
print(reduce(item_mult, my_list))
