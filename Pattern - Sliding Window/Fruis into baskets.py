fruits = ['A', 'B', 'C', 'A', 'C']

window_start = 0
max_length = 0
fruits_frequency = {}

for window_end in range(len(fruits)):
    # add newly visited fruit to the dict
    new_fruit = fruits[window_end]
    if new_fruit not in fruits_frequency:
        fruits_frequency[new_fruit] = 0
    fruits_frequency[new_fruit] += 1

    # while number of fruits in the window > 2: window contract from the start
    while len(fruits_frequency) > 2:
        window_start_fruit = fruits[window_start]
        if fruits_frequency[window_start_fruit] == 1:
            del fruits_frequency[window_start_fruit]
        else:
            fruits_frequency[window_start_fruit] -= 1
        window_start += 1

    max_length = max(max_length, window_end - window_start + 1)

print(max_length)