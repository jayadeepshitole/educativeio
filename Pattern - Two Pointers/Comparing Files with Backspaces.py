str1 = "xp#"
str2 = "xyz###"

def compare_string(str1, str2):
    str1_ptr, str2_ptr = len(str1) - 1, len(str2) - 1

    while str1_ptr >= 0 and str2_ptr >= 0:
        if str1[str1_ptr] != '#' and str2[str2_ptr] != '#':
            if str1[str1_ptr] != str2[str2_ptr]:
                return False
            str1_ptr -= 1
            str2_ptr -= 1
        else:
            cnt_hash_str1, cnt_hash_str2 = 0, 0
            while str1_ptr >= 0 and str1[str1_ptr] == '#':
                cnt_hash_str1 += 1
                str1_ptr -= 1
            while str2_ptr >= 0 and str2[str2_ptr] == '#':
                cnt_hash_str2 += 1
                str2_ptr -= 1
            str1_ptr -= cnt_hash_str1
            str2_ptr -= cnt_hash_str2

    if str1_ptr >= 0 or str2_ptr >= 0:
        return False

    return True

print(compare_string(str1, str2))