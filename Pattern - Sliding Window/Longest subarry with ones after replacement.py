arr = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
k = 3

window_start = 0
max_length = 0
cnt_zero = 0

for window_end in range(len(arr)):
    right_num = arr[window_end]
    if right_num == 0:
        cnt_zero += 1
        while cnt_zero > k:
            left_num = arr[window_start]
            if left_num == 0:
                cnt_zero -= 1

            window_start += 1

    max_length = max(max_length, window_end - window_start + 1)

print(max_length)

