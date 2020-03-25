arr = [2, 0, -1, 1, -2, 2]
target = 2

arr.sort()
n = len(arr)
quadruplets = []

for i in range(n - 3):
    first_num = arr[i]
    for j in range(i + 1, n - 2):
        sec_num = arr[j]
        left, right = j + 1, n - 1

        while left < right:
            curr_sum = arr[left] + arr[right]
            if (target - first_num - sec_num) < curr_sum:
                right -= 1
            elif (target - first_num - sec_num) > curr_sum:
                left += 1
            else:
                if sorted([first_num, sec_num, arr[left], arr[right]]) not in quadruplets:
                    quadruplets.append(list(sorted([first_num, sec_num, arr[left], arr[right]])))
                left += 1
                right -= 1

print(quadruplets)

