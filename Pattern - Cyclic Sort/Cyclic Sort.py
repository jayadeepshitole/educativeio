a = [1, 5, 6, 4, 3, 2]

for i in range(len(a)):
    if a[i] - 1  == i:
        continue
    else:
        current_num = a[i]
        while a[current_num - 1] != current_num:
            a[current_num - 1], current_num = current_num, a[current_num - 1]

print(a)