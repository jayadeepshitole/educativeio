arr = [2, 3, 3, 3, 6, 9, 9]
target_sum = 9

left_ptr, right_ptr = 0, len(arr) - 1

while left_ptr < right_ptr:
    if arr[left_ptr] + arr[right_ptr] == target_sum:
        print([left_ptr, right_ptr])
        break
    elif arr[left_ptr] + arr[right_ptr] < target_sum:
        left_ptr += 1
    else:
        right_ptr -= 1

if left_ptr == right_ptr:
    print('cant do it!')