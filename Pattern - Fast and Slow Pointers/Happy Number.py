def calcualte_sum_squares(num):
    ss = 0
    while num != 0:
        ss += (num%10)**2
        num = num//10
    return ss

def is_happy_num(num):
    if num == 0:
        return False

    ss_num = num
    num_seen = set([num])
    while True:
        ss_num = calcualte_sum_squares(ss_num)

        if ss_num == 1:
            return True
        elif ss_num in num_seen:
            return False

        num_seen.add(ss_num)

print(is_happy_num(12))