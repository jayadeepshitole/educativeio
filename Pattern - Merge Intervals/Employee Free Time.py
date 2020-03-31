class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + "," + str(self.end) + "]")


schedule = [[Interval(1, 3), Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]

# find the max end time
max_end_time = 0
for i in range(len(schedule)):
    for j in range(len(schedule[i])):
        max_end_time = max(max_end_time, schedule[i][j].end)

free_time_schedule = []
for i in range(len(schedule)):
    free_time = []
    current = schedule[i][0]
    for j in range(1, len(schedule[i])):
        if current.end < schedule[i][j].start:
            free_time.append(Interval(current.end, schedule[i][j].start))
            current = schedule[i][j]
    if current.end < max_end_time:
        free_time.append(Interval(current.end, max_end_time))
    free_time_schedule.append(free_time)


current_free_times = free_time_schedule[0]
for k in range(1, len(free_time_schedule)):
    next_free_times = free_time_schedule[k]
    free_time_overlap = []

    for l in range(len(current_free_times)):
        for j in range(len(next_free_times)):
            if max(current_free_times[l].start, next_free_times[j].start) \
                    < min(current_free_times[l].end, next_free_times[j].end):
                free_time_overlap.append(Interval(max(current_free_times[l].start, next_free_times[j].start),
                                          min(current_free_times[l].end, next_free_times[j].end)))
    current_free_times = free_time_overlap

result = []
for i in range(len(current_free_times)):
    result.append([current_free_times[i].start, current_free_times[i].end])

print(result)

