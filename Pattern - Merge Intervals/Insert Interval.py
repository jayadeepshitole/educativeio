intervals=[[1,3],[5,7],[8,12], [15, 17]]
new_interval = [4,10]

merged = []
i = 0
# append all the ones which are not overlapping and smaller
while i < len(intervals) and intervals[i][1] < new_interval[0]:
    merged.append(intervals[i])
    i += 1

# append all the ones which are overlapping
start = new_interval[0]
end = new_interval[1]
while i < len(intervals) and start <= intervals[i][0] <= end:
    start = min(start, intervals[i][0])
    end = max(end, intervals[i][1])
    i += 1

merged.append([start, end])

# append all the ones which are not overlapping and larger
while i < len(intervals) and intervals[i][0] > end:
    merged.append(intervals[i])
    i += 1

print(merged)