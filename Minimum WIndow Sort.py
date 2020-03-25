arr = [1, 2, 5, 3, 7, 10, 9, 12]

max_untill_now = []
max_num_seen = arr[0]
for i in range(len(arr)):
    max_num_seen = max(max_num_seen, arr[i])
    max_untill_now.append(max_num_seen)

min_untill_now = []
min_num_seen = arr[len(arr) - 1]
for i in reversed(range(len(arr))):
    min_num_seen = min(min_num_seen, arr[i])
    min_untill_now.append(min_num_seen)
min_untill_now.reverse()

left = 0
while left < len(arr) and arr[left] == min_untill_now[left]:
    left += 1

right = len(arr) - 1
while right > 0 and arr[right] == max_untill_now[right]:
    right -= 1
