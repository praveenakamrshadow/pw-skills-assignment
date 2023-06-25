def containsDuplicate(nums):
    unique_nums = set()
    for num in nums:
        if num in unique_nums:
            return True
        unique_nums.add(num)
    return False

nums = [1, 2, 3, 1]
result = containsDuplicate(nums)
print(result)
