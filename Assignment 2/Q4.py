def findLHS(nums):
    num_count = {}
    longest_subsequence = 0

    for num in nums:
        num_count[num] = num_count.get(num, 0) + 1

    for num in nums:
        if num + 1 in num_count:
            length = num_count[num] + num_count[num + 1]
            longest_subsequence = max(longest_subsequence, length)

    return longest_subsequence


nums = [1, 3, 2, 2, 5, 2, 3, 7]
result = findLHS(nums)
print(result)
