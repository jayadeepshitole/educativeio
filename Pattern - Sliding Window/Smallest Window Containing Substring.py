import collections
import math

str = 'abdabca'
pattern = 'abc'

pattern_char_freq = dict(collections.Counter(list(pattern)))
min_len_window = math.inf
window_start = 0

for window_end in range(len(str)):
    right_char = str[window_end]
    # update the window
    if right_char in pattern_char_freq:
        pattern_char_freq[right_char] -= 1

    # if pattern in window: shrink the window from start until the pattern is not in the window
    while max(pattern_char_freq.values()) <= 0:  # while pattern in the window
        # shrink the window
        left_char = str[window_start]
        if left_char in pattern_char_freq:
            if pattern_char_freq[left_char] == 0:
                # update min length
                min_len_window = min(min_len_window, window_end - window_start + 1)
            # update pattern char freq
            pattern_char_freq[left_char] += 1
        window_start += 1

    print('patter char freq:')
    print(pattern_char_freq)


print(min_len_window)