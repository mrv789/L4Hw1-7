from itertools import count

my_cont = count(int(input('put number: ')))
for i in range(10):
    print(next(my_cont))


import random
from itertools import cycle

my_list = []
for i in input('write any wordss: ').split():
    my_list.append(i)
    # my_list.append(int(i))

for i in input('write any numders: ').split():
    my_list.append(int(i))

    random.shuffle(my_list)

print(my_list)
my_cycle = cycle(my_list)
for i in range(10):
    print(next(my_cycle))
