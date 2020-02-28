str = "oidbcaf"
pattern="abc"

pattern_char_freq = {}
for char in pattern:
    if char not in pattern_char_freq:
        pattern_char_freq[char] = 0
    pattern_char_freq[char] += 1

window_char_freq = {}
for char in str[:len(pattern)]:
    if char not in window_char_freq:
        window_char_freq[char] = 0
    window_char_freq[char] += 1

if window_char_freq == pattern_char_freq:
    print(True)

for window_end in range(len(pattern), len(str)):
    window_start = window_end - len(pattern)
    left_char = str[window_start]
    window_char_freq[left_char] -= 1
    if window_char_freq[left_char] == 0:
        del window_char_freq[left_char]
    right_char = str[window_end]
    if right_char not in window_char_freq:
        window_char_freq[right_char] = 0
    window_char_freq[right_char] += 1
    # print()
    # print(str(window_start) + ':' + str(window_end))
    # print(window_char_freq)

    if window_char_freq == pattern_char_freq:
        print(True)
        break

