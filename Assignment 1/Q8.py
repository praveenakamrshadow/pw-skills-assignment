def findErrorNums(nums):
    n = len(nums)
    num_set = set()
    duplicate = -1
    missing = -1

    for num in nums:
        if num in num_set:
            duplicate = num
        num_set.add(num)

    for i in range(1, n + 1):
        if i not in num_set:
            missing = i
            break

    return [duplicate, missing]

nums = [1, 2, 2, 4]
result = findErrorNums(nums)
print(result)
