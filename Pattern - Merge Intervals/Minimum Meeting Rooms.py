intervals = [[4,5], [2,3], [2,4], [3,5]]
intervals.sort(key=lambda x:x[0])

start, end = 0, 1
num_rooms_available_after = {intervals[0][end] : 1}

for i in range(1, len(intervals)):
    latest_available_by = min(num_rooms_available_after)

    # room available
    if intervals[i][start] >= latest_available_by:
        num_rooms_available_after[latest_available_by] -= 1
        if num_rooms_available_after[latest_available_by] == 0:
            del num_rooms_available_after[latest_available_by]

        if intervals[i][end] not in num_rooms_available_after:
            num_rooms_available_after[intervals[i][end]] = 0
        num_rooms_available_after[intervals[i][end]] += 1
    else:
        if intervals[i][end] not in num_rooms_available_after:
            num_rooms_available_after[intervals[i][end]] = 0

        num_rooms_available_after[intervals[i][end]] += 1

print(sum(num_rooms_available_after.values()))