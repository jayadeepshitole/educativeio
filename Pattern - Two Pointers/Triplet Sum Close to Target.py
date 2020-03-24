import math

def search_best_pair(arr, target):
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

    return best_pair


arr = [-2, 0, 1, 2]
arr.sort()
target = 2
best_triplet = []
best_triplet_sum = math.inf

for i in range(len(arr) -2):
    current_element = arr[i]
    new_target = target - current_element
    best_pair = search_best_pair(arr[i + 1:], new_target)

    current_sum = sum(best_pair) + current_element
    if (abs(current_sum - target) < abs(best_triplet_sum - target)) or \
            (abs(current_sum - target) == abs(best_triplet_sum - target) and current_sum < best_triplet_sum):
        best_triplet = [current_element, best_pair[0], best_pair[1]]
        best_triplet_sum = current_sum

    print(current_element)
    print(best_pair)
    print(best_triplet)
    print()

print(best_triplet)