nums = [4, 2, 3, 1]

i = 0
while i < len(nums):
    j = nums[i]
    if nums[i] < len(nums) and nums[i] != nums[j]:
        nums[j], nums[i] = nums[i], nums[j]
    else:
        i += 1

for i in range(len(nums)):
    if nums[i] != i:
        print(i)

# print(len(nums))
