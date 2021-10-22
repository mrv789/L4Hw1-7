from functools import reduce


def sum_nums(a, b):
    return a + b


list = [i for i in range(100, 1001) if i % 2 == 0]
# print(list)

print(reduce(sum_nums, list))
