def moveZeroes(nums):
    zero_idx = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero_idx] = nums[zero_idx], nums[i]
            zero_idx += 1

nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)
