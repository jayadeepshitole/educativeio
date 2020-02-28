import collections

str = "abbcabc"
pattern = "abc"
n, k = len(str), len(pattern)

output_index_list = []
pattern_char_freq = dict(collections.Counter(list(pattern)))
window_char_freq = dict(collections.Counter(list(str)[:k]))

if pattern_char_freq == window_char_freq:
    output_index_list.append(0)

for window_end in range(k, n):
    window_start = window_end - k + 1
    remove_left_char = str[window_start - 1]
    add_right_char = str[window_end]

    window_char_freq[remove_left_char] -= 1
    if window_char_freq[remove_left_char] == 0:
        del window_char_freq[remove_left_char]

    if add_right_char not in window_char_freq:
        window_char_freq[add_right_char] = 0
    window_char_freq[add_right_char] += 1

    # print(window_char_freq)
    if window_char_freq == pattern_char_freq:
        output_index_list.append(window_start)

print(output_index_list)