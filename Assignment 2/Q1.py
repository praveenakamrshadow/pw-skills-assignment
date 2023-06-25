def arrayPairSum(nums):
    nums.sort()  # Sort the array in ascending order
    pair_sum = 0

    for i in range(0, len(nums), 2):
        pair_sum += nums[i]  # Add the minimum value of each pair to the sum

    return pair_sum

nums = [1, 4, 3, 2]
result = arrayPairSum(nums)
print(result)
