arr = [2, 5, 3, 10]
target = 30

sub_arrays = []
for i in range(len(arr)):
    product = arr[i]
    sub_array = [arr[i]]
    j = i + 1

    while j < len(arr) and product < target:
        sub_arrays.append(list(sub_array))

        product *= arr[j]
        sub_array.append(arr[j])
        j += 1

print(sub_arrays)