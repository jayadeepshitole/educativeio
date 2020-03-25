arr = [2, 2, 0, 1, 2, 0]

# Push all 0's to the beginning
low = 0
while arr[low] == 0 and low < len(arr):
    low += 1

for i in range(0, len(arr)):
    if i < low:
        continue

    if arr[i] == 0:
        arr[i], arr[low] = arr[low], arr[i]

        while arr[low] == 0 and low < len(arr):
            low += 1

    if low == len(arr):
        break

# Push all 2's to the end
high = len(arr) - 1
while arr[high] == 2 and high > 0:
    high -= 1

for i in range(len(arr), 0, -1):
    if i > high:
        continue

    if arr[i] == 2:
        arr[i], arr[high] = arr[high], arr[i]

        while arr[high] == 2 and high > 0:
            high -= 1

    if high < 0:
        break

print(arr)