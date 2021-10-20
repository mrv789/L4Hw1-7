def per_salary (num_1, num_2, num_3):
    result = (num_1 * num_2) + num_3
    return result

num_1 = int(input("Введите отработанное время: "))
num_2 = int(input("Введите ставку за 1 час: "))
num_3 = int(input("Введите сумму премии: "))
total = per_salary (num_1=num_1, num_2=num_2, num_3=num_3)

print(f'Итого сумма выплаты составляет {total} рублей')


