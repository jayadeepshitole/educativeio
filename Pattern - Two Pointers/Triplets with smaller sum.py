def find_relevant_pairs(arr, target):
    left, right = 0, len(arr) - 1
    num_rel_pairs = 0

    while left < right:
        cur_sum = arr[left] + arr[right]

        if cur_sum < target:
            num_rel_pairs += (right - left)
            left += 1
        elif cur_sum >= target:
            right -= 1
    return num_rel_pairs


arr = [-1, 4, 2, 1, 3]
arr.sort()
target = 5
num_triplets = 0

for i in range(len(arr)):
    cur_ele = arr[i]
    new_target = target - cur_ele

    num_rel_pairs = find_relevant_pairs(arr[i + 1:], new_target)
    num_triplets += num_rel_pairs

print(num_triplets)