from __future__ import print_function


class interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + "," + str(self.end) + "]", end='')


intervals = [interval(1, 4), interval(6, 3), interval(2, 5)]
intervals.sort(key=lambda x: x.start)

merged_intervals = []

i = 0
while i <= len(intervals) - 1:
    if i == len(intervals) - 1:
        merged_intervals.append(intervals[i])
        break

    curr_int_beg, curr_int_end = intervals[i].start, intervals[i].end
    while i <= len(intervals) - 2:
        next_int_beg, next_int_end = intervals[i + 1].start, intervals[i + 1].end

        # case 1: they dont overlap
        if curr_int_end < next_int_beg:
            merged_intervals.append(interval(curr_int_beg, curr_int_end))
            i += 1
            break
        else: # there is a overlap
            curr_int_end = max(curr_int_end, next_int_end)
            i += 1

            if i == len(intervals) - 1:
                merged_intervals.append(interval(curr_int_beg, curr_int_end))
                i += 1
                break


for i in merged_intervals:
    i.print_interval()