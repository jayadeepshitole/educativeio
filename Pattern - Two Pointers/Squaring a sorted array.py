
arr = [-2, -1, 0, 2, 3]
squared_sorted_arr = [0] * len(arr)
ind_element_smallest_abs_val = 0
smallest_abs_value = abs(arr[0])

for ind in range(1, len(arr)):
    if smallest_abs_value > abs(arr[ind]):
        smallest_abs_value = abs(arr[ind])
        ind_element_smallest_abs_val = ind

squared_sorted_arr[0] = arr[ind_element_smallest_abs_val]**2
back_ptr = ind_element_smallest_abs_val - 1
front_ptr = ind_element_smallest_abs_val + 1

i = 1
while back_ptr >= 0 or front_ptr <= len(arr) - 1:
    if back_ptr < 0:
        squared_sorted_arr[i] = arr[front_ptr] ** 2
        front_ptr += 1
    elif front_ptr == len(arr):
        squared_sorted_arr[i] = arr[back_ptr] ** 2
        back_ptr -= 1
    elif abs(arr[back_ptr]) < abs(arr[front_ptr]):
        squared_sorted_arr[i] = arr[back_ptr]**2
        back_ptr -= 1
    else:
        squared_sorted_arr[i] = arr[front_ptr]**2
        front_ptr += 1
    i += 1

print(squared_sorted_arr)