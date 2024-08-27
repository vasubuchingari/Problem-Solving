#INSERTION sorting ascending

nums = [5, 4, 3, 2, 1]
for i in range(1, len(nums)):
    current_value = nums[i]
    position = i
    while position > 0 and current_value < nums[position - 1]:
        nums[position] = nums[position - 1]
        position = position - 1
    nums[position] = current_value
print(nums)
