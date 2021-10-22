
def factor_gen(number):
    current = int(input('write number: '))
    for i in range(1, number + 1):
        current *= i
        yield current


n = int(input('write steps: '))
for i in factor_gen(n):
    print(i)