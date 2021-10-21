a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


my_list_new = [a[i] for i in range(1, len(a)) if a[i] > a[i - 1]]

print(my_list_new)
