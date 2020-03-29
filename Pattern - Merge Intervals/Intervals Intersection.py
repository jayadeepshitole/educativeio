arr1 = [[1, 3], [5, 6], [7, 12]]
arr2 = [[2, 3], [5, 7]]

merged = []
ind1, ind2 = 0, 0

while ind1 < len(arr1) and ind2 < len(arr2):
    # no overlap - arr1 list is smaller
    if arr1[ind1][1] < arr2[ind2][0]:
        ind1 += 1
    elif arr2[ind2][1] < arr1[ind1][0]:
        ind2 += 1
    else: # overlap case
        merged.append(list([max(arr1[ind1][0], arr2[ind2][0]), min(arr1[ind1][1], arr2[ind2][1])]))
        if arr1[ind1][1] > arr2[ind2][1]:
            ind2 += 1
        elif arr1[ind1][1] < arr2[ind2][1]:
            ind1 += 1
        else:
            ind1 += 1
            ind2 += 1

print(merged)