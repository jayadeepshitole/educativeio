arr = [-2, 0, 1, 2]
target = 0

import math

best_pair_sum = math.inf
best_abs_gap = math.inf
best_pair = []
left, right = 0, len(arr) - 1

while left < right:
    current_sum = arr[left] + arr[right]

    if abs(target - current_sum) < best_abs_gap or \
            (abs(target - current_sum) == best_abs_gap and current_sum < best_pair_sum):
        best_abs_gap = abs(target - current_sum)
        best_pair_sum = current_sum
        best_pair = [arr[left], arr[right]]

    if current_sum < target:
        left += 1
    elif current_sum > target:
        right -= 1
    else:
        break

