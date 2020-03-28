arr = [1, 2, -1, 2, 2]

def find_next_index(current_index, is_forward, arr):
    current_element = arr[current_index]

    if is_forward and current_element < 0 or not is_forward and current_element > 0:
        return -1

    next_index = (current_index + current_element) % len(arr)
    return next_index

for i in range(len(arr)):
    slow_ind, fast_ind = i, i
    is_forward = arr[i] >= 0

    while True:
        slow_ind = find_next_index(slow_ind, is_forward, arr)
        fast_ind = find_next_index(fast_ind, is_forward, arr)

        if slow_ind == -1 or fast_ind == -1:
            break

        if fast_ind != -1:
            fast_ind = find_next_index(fast_ind, is_forward, arr)

        if slow_ind == fast_ind and fast_ind != -1:
            print(i)
            print('cycle found')
            break






