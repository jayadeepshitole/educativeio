strng = "aabccbb"

window_start = 0
max_length = 0
chars_in_window = set()

for window_end in range(len(strng)):
    right_char = strng[window_end]
    # if right_char in window move start until its not
    while right_char in chars_in_window:
        left_char = strng[window_start]
        chars_in_window.remove(left_char)
        window_start += 1

    # add right char to window
    chars_in_window.add(right_char)
    max_length = max(max_length, window_end - window_start + 1)

print(max_length)