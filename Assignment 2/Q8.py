def minimumScore(nums, k):
    min_val = min(nums)
    max_val = max(nums)

    if min_val + k >= max_val - k:
        return 0
    else:
        return max_val - k - (min_val + k)


nums = [1]
k = 0
result = minimumScore(nums, k)
print(result)
