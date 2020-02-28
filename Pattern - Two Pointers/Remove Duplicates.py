arr = [2, 2, 2, 11]

last_unique_element = arr[0]
update_index = 1

for ind in range(1, len(arr)):
    current_element = arr[ind]
    if current_element != last_unique_element:
        arr[update_index] = current_element
        update_index += 1
        last_unique_element = current_element

print(update_index)
print(arr)