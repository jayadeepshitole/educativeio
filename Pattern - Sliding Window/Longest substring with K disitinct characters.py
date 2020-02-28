str = 'cbbebi'
k = 1
# longest_string = ''
#
# # # naive solution - O(n^2)
# for start_index in range(len(str)):
#     visited_chars = set(str[start_index])
#     end_index = start_index + 1
#
#     while end_index < len(str):
#         visited_chars.add(str[end_index])
#         if len(visited_chars) > k:
#             end_index = end_index - 1
#             len_current_string = end_index - start_index + 1
#             if len(longest_string) <= len_current_string:
#                 longest_string = str[start_index: end_index + 1]
#             break
#         end_index += 1
#
#     if end_index == len(str):
#         end_index = end_index - 1
#         len_current_string = end_index - start_index + 1
#         if len(longest_string) <= len_current_string:
#             longest_string = str[start_index: end_index + 1]
#
#     # print('staring index:' + str(start_index))
#     # print('longest string: '+ longest_string)
# print(longest_string)

# Smart solution - O(n)
end_index = 1
start_index = 0
visited_chars = set(str[start_index])
visited_chars_cnt = dict()
visited_chars_cnt[str[start_index]] = 1
longest_string = str[start_index]

for start_index in range(1, len(str)):
    # remove last start_index character from visited chars
    first_char = str[start_index - 1]
    visited_chars_cnt[first_char] -= 1
    if visited_chars_cnt[first_char] == 0:
        visited_chars.remove(first_char)

    while end_index < len(str):
        new_char_visited = str[end_index]
        if new_char_visited not in visited_chars_cnt:
            visited_chars_cnt[new_char_visited] = 1
        else:
            visited_chars_cnt[new_char_visited] += 1
        visited_chars.add(str[end_index])

        if len(visited_chars) > k:
            end_index = end_index - 1
            len_current_string = end_index - start_index + 1
            if len(longest_string) <= len_current_string:
                longest_string = str[start_index: end_index + 1]
            break
        end_index += 1

    if end_index == len(str):
        end_index = end_index - 1
        len_current_string = end_index - start_index + 1
        if len(longest_string) <= len_current_string:
            longest_string = str[start_index: end_index + 1]
        break

    # print('staring index:' + str(start_index))
    # print('longest string: '+ longest_string)
print(longest_string)
