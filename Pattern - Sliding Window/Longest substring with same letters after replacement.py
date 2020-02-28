strng: str = 'abbcb'
k = 1

window_start = 0
max_length = 0
char_freq = {}

for window_end in range(len(strng)):
    right_char = strng[window_end]
    if right_char not in char_freq:
        char_freq[right_char] = 0
    char_freq[right_char] += 1

    # shrink the window so that the combined freq of all the chars excluding max freq char > k
    while sum(char_freq.values()) - max(char_freq.values()) > k:
        # update char freq mapping
        left_char = strng[window_start]
        char_freq[left_char] -= 1
        if char_freq[left_char] == 0:
            del char_freq[left_char]

        window_start += 1

    # update max length
    max_length = max(max_length, window_end - window_start + 1)

print(max_length)
