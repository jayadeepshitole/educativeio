import collections
string = 'catcatfoxfox'
words = ['cat', 'fox']

valid_window_start_ind = []
words_freq_map = dict(collections.Counter(words))
window_start = 0
if len(words) > 0:
    word_len = len(words[0])

for window_end in range(word_len - 1, len(string), word_len):
    right_word = string[window_end - word_len + 1: window_end + 1]
    words_freq_map[right_word] -= 1

    while window_end - window_start + 1 > len(words) * word_len:
        left_word = string[window_start: window_start + word_len]
        words_freq_map[left_word] += 1
        window_start += word_len

    if max(words_freq_map.values()) == 0 and min(words_freq_map.values()) == 0 \
            and (window_end - window_start + 1) == (len(words) * word_len):
        valid_window_start_ind.append(window_start)

print(valid_window_start_ind)
